import global_defs as utils

bit_len: int
cells_per_bank: int
total_cells: int

cell_block = []
banks = {}
current_bank: int

display_width: int
display_height: int
display_bank = ""

def init(bit_length, block_cells, num_banks, dis_w, dis_h):
    global cells_per_bank, display_height, display_width, cell_block, banks, current_bank, total_cells, display_bank

    bit_len = bit_length
    cells_per_bank = block_cells
    
    for i in range(num_banks):
        key = format(i, "04b")

        # Build a fresh block of cells for this bank
        block = []
        for j in range(cells_per_bank):
            block.append([False] * bit_len)

        banks[key] = block

    total_cells = num_banks * cells_per_bank
    
    current_bank = "0" * (bit_length // 2)

    # Display setup
    display_width = dis_w
    display_height = dis_h

    display_bank = "1" * (bit_length // 2)
    display_bytes = (display_width * display_height) // bit_len
    resolution = display_width * display_height
    

def read(cell):
    value = banks[current_bank][utils.bits_to_int(cell)]
    return value

def write(cell, value):
    banks[current_bank][utils.bits_to_int(cell)] = value

def change_bank(bank):
    global current_bank
    current_bank = bank
    print("Current Bank: " + current_bank)
