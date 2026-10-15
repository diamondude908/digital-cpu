import global_defs as utils

class Memory():
    def __init__(self, bit_len, cells):
        self.bit_len = bit_len
        self.cells = [[False]*bit_len for i in range(cells)]

    def read(self, cell):
        value = self.cells[utils.bits_to_int(cell)]
        print(value)
        return value

    def write(self, cell, value):
        self.cells[utils.bits_to_int(cell)] = value
        