from cpu import CPU

while True:
    user_input = input(">>> ")
    parts = user_input.split()
    result = []

    if user_input == "exit":
            break
    if len(parts) > 1:
        opcode = parts[0]
        a = parts[1]
        b = parts[2]
        c = parts[3]

        print_result = CPU.execute_instruction(opcode, a, b, c)

        print(print_result)
    else:
        SyntaxError(opcode + " is not a valid opcode")