import programs.isa as isa
import global_defs as utils

class Assembler():

    def __init__(self, bit_len, num_reg):
        self.bit_len = bit_len
        self.inst_len = bit_len * 2
        self.num_reg = num_reg
        self.program = []

        self.labels = {}
        self.registers = {}
        self.macros = {}
        for i in range(num_reg):
            self.registers["r" + str(i)] = format(i, "04b")

        # Initialize the ISA lists

        self.opcodes = isa.opcodes
        self.psuedos = isa.pseudos

    # Reads the .txt file given by the CPU and 
    # turns it into a list of strings

    def read_file(self, file: str):
        cleaned = []
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line[0] == "#":
                    continue
                
                cleaned.append(line)

        expanded = self.expand_macros(cleaned)

        return expanded

    # Formats each line into one continueous instruction of binary digits 

    def format_line(self, parts: list):
        # Format the opcode into binary
        oc = parts[0]
        if oc not in self.opcodes:
            raise SyntaxError(oc + " is not a valid instruction")
        parts[0] = self.opcodes[oc]

        # Format registers and hex into binary

        for i in range(1, len(parts)):

            if parts[i] in self.registers:
                parts[i] = self.registers[parts[i]]

            elif parts[i].startswith("0x"):
                value = int(parts[i], 16)
                if value > 255:
                    raise SyntaxError(value + " is not valid 8 bit number.")
                parts[i] = format(value, "08b")

        # Puts everything together

        new_line = "".join(parts)
        new_line = new_line.ljust(self.inst_len, "0")

        return new_line

    def resolve_labels(self, line, prog):
        if line[0].endswith(":"):
            name = line[0][:-1]
            self.labels[name] = len(prog)
            return
        elif line[-1] in self.labels:
            line[-1] = format(self.labels[line[-1]], "08b")
            return line
        else:
            return line

    def expand_macros(self, lines):
        body_lines = []
        i = 0
        while i < len(lines):
            parts = lines[i].split()

            if parts[0] == "MACRO":
                name = parts[1]
                params = parts[2:]
                macro_lines = []
                i += 1
                while lines[i] != "ENDMACRO":
                    macro_lines.append(lines[i])
                    i += 1
                self.macros[name] = [params, macro_lines]
            else:
                body_lines.append(lines[i])

            i += 1
        result = []
        for line in body_lines:
            parts = line.split()

            if parts[0] in self.macros:
                current_macro = parts[0]
                params = self.macros[current_macro][0]
                macro_lines = self.macros[current_macro][1]
                args = parts[1:]
                if len(args) != len(params):
                    raise SyntaxError("Macro " + current_macro + " expects " + len(params) + " arguements.") 

                for macro_line in macro_lines:
                    new_parts = []
                    for part in macro_line.split():
                        if part in params:
                            new_parts.append(args[params.index(part)])
                        else:
                            new_parts.append(part)
                    result.append(" ".join(new_parts))
            else:
                result.append(line)

        return result

        
    def expand_psuedos(self, parts):
        if parts[0] not in self.psuedos:
            return [parts]

        if parts[0] in self.psuedos:
            oc = parts[0]
            dest = ""
            src1 = ""
            src2 = ""

            if len(parts) > 1:
                dest = parts[1]
            if len(parts) > 2:
                src1 = parts[2]
            if len(parts) > 3:
                src2 = parts[3]
                
            result = []

            for inst in self.psuedos[oc]:
                new_inst = []

                for part in inst:
                    match part:
                        case "dest":
                             new_inst.append(dest)
                        case "src1":
                            new_inst.append(src1)
                        case "src2":
                            new_inst.append(src2)
                        case "label":
                            new_inst.append(parts[-1])
                        case _:
                            if len(part) == 4:
                                new_inst.append(part)
                            elif part in self.opcodes or part in self.registers:
                                new_inst.append(part)
                            else:
                                raise SyntaxError(part + " is not a valid psudeo-instruction parameter.")
                result.append(new_inst)

            return result

    # Formats each line in the entire program

    def format_program(self, prog):
        # Formats the program into all real instructions
        labels_resolved = []
        expanded = []

        # Expands any pseudos that currently reside in the program
        for line in prog:
            parts = line.split()
            
            for inst in self.expand_psuedos(parts):
                expanded.append(inst)

        # Resolves any labels that need to be dealt with
        for line in expanded:
            new_line = self.resolve_labels(line, labels_resolved)
            if new_line:
                labels_resolved.append(new_line)

        print(self.labels)
        print(labels_resolved)

        # Formats every line into binary
        formatted = []
        for inst in labels_resolved:
            formatted.append(self.format_line(inst))
        return formatted



