import global_defs as utils

bit_len: int
registers = []

def get_info(num_registers, bit_len):
    global registers
    bit_len = bit_len

    def_val = format(0, f"0{bit_len}b")
    registers = [utils.binary(def_val)] * num_registers

def read(dest):
   return registers[utils.bits_to_int(dest)]

def write(dest, value):
    index = utils.bits_to_int(dest)
    registers[index] = value
    
    return registers[index]

operations = ["READ", "LDI"]

def operate(opcode, dest, value):

        if opcode in operations:
            match opcode:
                case "READ":
                    return read(dest)
                case "LDI":
                    return write(dest, value)