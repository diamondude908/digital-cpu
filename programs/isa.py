
opcodes = {
   "CBK": "0000",
   "ADD": "0001",
   "SUB": "0010",
   "AND": "0011",
   "OR": "0100",
   "XOR": "0101",
   "SFT": "0110",
   "NOT": "0111",
   "DIS": "1000",
   "LD": "1001",
   "LDI": "1010",
   "CMP": "1011",
   "STR": "1100",
   "JMP": "1101",
   "CMP": "1110",
   "HLT": "1111"
}

bin_opcodes = {
    "0000": "CBK",
    "0001": "ADD",
    "0010": "SUB",
    "0011": "AND",
    "0100": "OR",
    "0101": "XOR",
    "0110": "SFT",
    "0111": "NOT",
    "1000": "DIS",
    "1001": "LD",
    "1010": "LDI",
    "1100": "STR",
    "1101": "JMP",
    "1110": "CMP",
    "1111": "HLT"
}

pseudos = {
    # Jump operations

    "JZ": [["JMP", "0010", "label"]],
    "JNZ": [["JMP", "0011", "label"]],
    "JC": [["JMP", "0100", "label"]],
    "JNC": [["JMP", "0101", "label"]],

    # ALU based operations

    "MOVE": [["ADD", "dest", "src1", "r0"]],
    "SHL": [["SFT", "0001", "dest", "src1"]],
    "SHR": [["SFT", "0010", "dest", "src1"]],
    "ADDI": [["LDI", "r15", "src1"], ["ADD", "dest", "dest", "r15"]],

    # Negative ALU operations

    "NAND": [["AND", "dest", "src1", "src2"], ["NOT", "dest", "dest"]],
    "NOR": [["OR", "dest", "src1", "src2"], ["NOT", "dest", "dest"]],
    "XNOR": [["XOR", "dest", "src1", "src2"], ["NOT", "dest", "dest"]],

    # Display operations
    

    # Miscellaneous operations

    "NOP": [["ADD", "r0", "r0", "r0"]]
}

