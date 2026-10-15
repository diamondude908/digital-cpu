
class Assembler():

    def __init__(self, bit_len):
        self.bit_len = bit_len
        self.inst_len = bit_len * 2
        self.program = []

        # List of all opcodes and their binary equivalents

        self.opcodes = {
            "NOP": "0000",
            "ADD": "0001",
            "SUB": "0010",
            "AND": "0011",
            "OR": "0100",
            "XOR": "0101",
            "SHL": "0110",
            "SHR": "0111",
            "MOV": "1000",
            "LD": "1001",
            "LDI": "1010",
            "CMP": "1011",
            "STR": "1100",
            "JMP": "1101",
            "JZ": "1110",
            "HLT": "1111"
        }

        self.psuedos = [
            "JZ",
            "JNZ"
        ]

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

        oc = parts[0]

        if oc in self.opcodes:
            parts[0] = self.opcodes[oc]
        elif oc in self.psuedos:
            self.assemble_psuedo(parts)
        else:
            print(oc + " is not a valid instruction")

        new_line = "".join(parts)

        new_line = new_line.ljust(self.inst_len, "0")
        
        return new_line

    def assemble_psuedo(self, tokens):
        oc = tokens[0]
        dest = tokens[1]
        src1 = None
        src2 = None

        if len(tokens) > 2:
            src1 = tokens[2]
            src2 = tokens[3]

        result = []

        if oc in self.psuedos:
            match oc:
                case "JZ":
                    print("JZ")
                    inst = "JUMP 0010" + dest
                    result.append(inst)
        print(result)
        return result

    # Formats each line in the entire program

    def format_program(self, prog):
        formatted = []
        for line in prog:
            formatted.append(self.format_line(line))

        return formatted


assembler = Assembler(8)
inst = "JZ 0001"

assembler.assemble_psuedo(inst)


