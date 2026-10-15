from cpu import CPU
from components.alu import ALU
from programs.assembler import Assembler
from components.memory import Memory
import components.program_counter as Pc
import components.register_file as register_file
import global_defs as utils

bit_len = 8
num_reg = 16
cells = 256

cpu = CPU(bit_len, num_reg, ALU(bit_len), Pc, utils, register_file, Memory(bit_len, cells), Assembler(bit_len))

version = "beta 0.1"

print("Running: EthanOS, ver. " + version)

commands = ["exit", "run"]

def run_program(program):
    prog = "programs/" + program
    cpu.assemble_program(prog)
    cpu.run()

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
    