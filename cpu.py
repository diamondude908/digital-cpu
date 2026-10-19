import components.memory as Memory
from programs.assembler import Assembler
import global_defs as utils
import components.program_counter as Pc
import components.register_file as RegFile
from components.alu import ALU
import components.display as display

# CPU class

class CPU():

    def __init__(self, bit_len, num_reg, mem_cells, display_width, display_height):
        
        # Initialize bit information and registers
        
        self.bit_len = bit_len
        self.field_len = bit_len // 2
        self.num_registers = num_reg
        self.memory = Memory
        self.memory.init(bit_len, mem_cells, display_width, display_height)

        # Initialize all components

        self.pc = Pc
        self.utils = utils
        self.alu = ALU(bit_len)
        self.reg_file = RegFile
        self.reg_file.init(self.num_registers, bit_len)
        self.display = display
        self.display.init()
        # Initialize all program-related information

        self.cycles = 0
        self.flags = {}
        self.program = []
        self.assembler = Assembler(bit_len)

        # Initialize all opcodes from binary

        self.bin_to_op = {
            "0000": "NOP",
            "0001": "ADD",
            "0010": "SUB",
            "0011": "AND",
            "0100": "OR",
            "0101": "XOR",
            "0110": "SHL",
            "0111": "SHR",
            "1000": "MOV",
            "1001": "LD",
            "1010": "LDI",
            "1100": "STR",
            "1101": "JMP",
            "1110": "HLT",
            "1111": "CMP"
        }

        

    # The function that executes all instructions from the program

    def assemble_program(self, program):
        assemble = self.assembler

        unassembled = assemble.read_file(program)
        self.program = assemble.format_program(unassembled)
        self.pc.prog_len = len(self.program)
        
    # This assembles an instuction from a 16 bit double instruction
    # to four parts that are returned to the step function.
    # For example, "0001011000111010" becomes ["ADD", "0110", "0011", "1010"]

    def assemble_instruction(self, inst):
        size = len(inst) // 4
        parts = [inst[i * size:(i + 1) * size] for i in range(4)]

        oc = parts[0]
        if oc in self.bin_to_op:
            parts[0] = self.bin_to_op[oc]

        opcode = parts[0]
        dest = parts[1]
        src1 = parts[2]
        src2 = parts[3]

        return opcode, dest, src1, src2

    # This matches each of the arguements including the opcode, dest,
    # and sources to their proper instuction and runs the related component.


    def execute_instruction(self, opcode, dest, src1, src2):
        self.cycles += 1
        result = None
        flags = None

        reg_a = self.reg_file.read(src1)
        reg_b = self.reg_file.read(src2)

        src = self.utils.binary(src1 + src2)
        mem_dest = self.utils.binary(dest + src1)

        # This is only used in the JMP case
        int_dest = self.utils.bits_to_int(src1)

        match opcode:
            case "NOP":
                pass
            case "ADD" | "SUB" | "AND" | "OR" | "XOR": 
                result, flags = self.alu.operate(opcode, dest, reg_a, reg_b)
            case "SHL": 
                result, flags = self.alu.operate("SHL", dest, src, None)
            case "SHR": 
                result, flags = self.alu.operate("SHR", dest, src, None)
            case "MOV": 
                "1000"
            case "LD":
                mem_val = self.memory.read(src)
                self.reg_file.operate("LDI", dest, mem_val)
                print("Read: " + self.utils.display_bin(mem_val))
            case "LDI": 
                result = self.reg_file.operate("LDI", dest, src)
            case "CMP":
                # This one is in a weird order because comp only takes 
                # two arguments, so it takes the "write" address as the
                # zero register and uses the other two positions as normal
                _, flags = self.alu.operate("COMP", src2, dest, src1)
            case "STR": 
                self.memory.write(mem_dest, reg_b)
            case "JMP": 
                cond = int(dest, 2)
                conditions = {
                    0: True,
                    1: self.flags["Z"],
                    2: not self.flags["Z"],
                    3: self.flags["C"],
                    4: not self.flags["C"]
                }
                if conditions[cond]:
                    self.pc.jump(int_dest)
            case "HLT": 
                "1110"
            
            case _:
                SyntaxError(opcode + " is not a real opcode.")

        if flags is not None:
            self.flags = flags
        
        display_result = self.utils.display_bin(result)
        display_result = opcode + ": " + display_result
        return display_result

    # Takes the PC one step further into the program every time this
    # is called, and it executes the instruction at each step.

    def step(self):
        count = self.pc.counter

        op, dest, src1, src2 = self.assemble_instruction(self.program[count])

        out = self.execute_instruction(op, dest, src1, src2)
        if out:
            print(out)
        self.pc.increment()

    # The function that runs the entire program

    def run(self):
        while self.pc.counter < self.pc.prog_len:
            self.step()
        else:
            print("Program finished in " + str(self.cycles) + " cycles!")
            




    