import global_defs as utils

bit_len: int
num_cells: int
cells = []

display_width: int
display_height: int

def init(bit_length, mem_cells, dis_w, dis_h):
    global num_cells, display_height, display_width

    bit_len = bit_length
    num_cells = mem_cells
    cells = [[False]*bit_len for i in range(mem_cells)]

    # Display setup
    display_width = dis_w
    display_height = dis_h

    display_bytes = (display_width * display_height) // bit_len
    resolution = display_width * display_height
    

def read(cell):
    value = cells[utils.bits_to_int(cell)]
    return value

def write(cell, value):
    cells[utils.bits_to_int(cell)] = value


        