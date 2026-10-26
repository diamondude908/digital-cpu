import threading
from cpu import CPU

bit_len = 8
num_reg = 16
cells = 256
display_width = 32
display_height = 32

cpu = CPU(bit_len, num_reg, cells, display_width, display_height)

version = "beta 1.2"

print("Running: EthanOS, ver. " + version)
print("Current Resoltion: " + str(display_width) + "x" + str(display_height))

commands = ["exit", "run", "read"]

def run_program(program):
    prog = "programs/" + program
    cpu.assemble_program(prog)
    cpu.run()


#cpu.display.draw_pixel(0, 0, 1)
def shell_loop():
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
                    cpu.display.running = False
                    break
                case "run":
                    run_program(arg)
                case "read":
                    print(cpu.reg_file.read(arg))

        print("To exit, type in exit into the the text field.")

shell_thread = threading.Thread(target=shell_loop, daemon=True)
shell_thread.start()

print("starting window")
cpu.display.run_window()
print("window loop ended")
    