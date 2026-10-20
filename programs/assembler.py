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

    def format_line(self, line: str):
        parts = line.split()

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

    def assemble_psuedo(self, tokens):
        pass

    # Formats each line in the entire program

    def format_program(self, prog):
        formatted = []
        for line in prog:
            formatted.append(self.format_line(line))
        print(formatted)
        return formatted



