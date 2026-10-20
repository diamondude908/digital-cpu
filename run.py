from cpu import CPU

bit_len = 8
num_reg = 16
cells = 256
display_width = 16
display_height = 16

cpu = CPU(bit_len, num_reg, cells, display_width, display_height)

version = "beta 1.1"

print("Running: EthanOS, ver. " + version)
print("Current Resoltion: " + str(display_width) + "x" + str(display_height))

commands = ["exit", "run"]

def run_program(program):
    prog = "programs/" + program
    cpu.assemble_program(prog)
    cpu.run()


#cpu.display.draw_pixel(0, 0, 1)

while True:
    user_input = input(">>> ").lower()
    parts = user_input.split()
    command = parts[0]
    arg = None

    if len(parts) > 1:
        arg = parts[1]

    if command in commands:
        match command:
            case "exit":
                break
            case "run":
                run_program(arg)

    print("To exit, type in exit into the the text field.")
    