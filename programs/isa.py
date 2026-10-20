
opcodes = {
   "NOP": "0000",
   "ADD": "0001",
   "SUB": "0010",
   "AND": "0011",
   "OR": "0100",
   "XOR": "0101",
   "SFT": "0110",
   "DIS": "0111",
   "MOV": "1000",
   "LD": "1001",
   "LDI": "1010",
   "CMP": "1011",
   "STR": "1100",
   "JMP": "1101",
   "CMP": "1110",
   "HLT": "1111"
}

bin_opcodes = {
    "0000": "NOP",
    "0001": "ADD",
    "0010": "SUB",
    "0011": "AND",
    "0100": "OR",
    "0101": "XOR",
    "0110": "SFT",
    "0111": "DIS",
    "1000": "MOV",
    "1001": "LD",
    "1010": "LDI",
    "1100": "STR",
    "1101": "JMP",
    "1110": "CMP",
    "1111": "HLT"
}

pseudos = {
    # Jump operations

    "JZ": [["JMP", "0010", "dest"]],
    "JNZ": [["JMP", "0011", "dest"]],
    "JC": [["JMP", "0100", "dest"]],
    "JNC": [["JMP", "0101", "dest"]],

    # Negative ALU operations

    "NAND": [["AND", "dest", "src1", "src2"], ["NOT", "dest", "src1"]]
}

