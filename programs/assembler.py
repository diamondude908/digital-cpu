import programs.isa as isa
import global_defs as utils

class Assembler():

    def __init__(self, bit_len, num_reg):
        self.bit_len = bit_len
        self.inst_len = bit_len * 2
        self.num_reg = num_reg
        self.program = []

        self.registers = {}
        for i in range(num_reg):
            self.registers["r" + str(i)] = format(i, "04b")

        # Initialize the ISA lists

        self.opcodes = isa.opcodes
        self.psuedos = isa.pseudos

    # Reads the .txt file given by the CPU and 
    # turns it into a list of strings

    def read_file(self, file: str):
        list_file = []
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line[0] == "#":
                    continue
                list_file.append(line)
        return list_file

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

    def assemble_psuedo(self, parts):
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
                new_inst.append(inst[0])

                for part in inst:
                    match part:
                        case "dest":
                             new_inst.append(dest)
                        case "src1":
                            new_inst.append(src1)
                        case "src2":
                            new_inst.append(src2)
                        case _:
                            if len(part) == 4:
                                new_inst.append(part)
                            elif part not in self.opcodes:
                                raise SyntaxError(part + " is not a valid psudeo-instruction parameter.")
                print("New inst")
                print(new_inst)
                result.append(new_inst)

            return result

    # Formats each line in the entire program

    def format_program(self, prog):
        # Formats the program into all real instructions
        expanded = []
        for line in prog:
            parts = line.split()
            for inst in self.assemble_psuedo(parts):
                expanded.append(inst)

        # Formats every line into binary
        formatted = []
        for inst in expanded:
            formatted.append(self.format_line(inst))
        return formatted



