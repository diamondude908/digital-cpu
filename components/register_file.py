import global_defs

bit_len: int
utils = global_defs
registers = []

def get_info(num_registers, bit_len):
    global registers
    bit_len = bit_len

    def_val = format(0, f"0{bit_len}b")
    registers = [utils.binary(def_val)] * num_registers

def bits_to_int(bits) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | int(bit)
    return value


def read(dest):
   return registers[bits_to_int(dest)]

def write(dest, value):
    index = bits_to_int(dest)
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