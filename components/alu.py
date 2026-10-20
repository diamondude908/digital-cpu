import global_defs
import components.register_file

class ALU:

    def __init__(self, bit_len):
        self.bit_len = bit_len
        self.utils = global_defs
        self.reg_file = components.register_file

    def AND(self, a, b):
        return a & b

    def OR(self, a, b):
        return a | b

    def XOR(self, a, b):
        return a ^ b

    def NOT(self, a):
        return not a

    def get_inverse(self, a):
        return [self.NOT(c) for c in a]

    def half_add(self, a, b):
        sum = False
        carry = False

        if self.XOR(a, b):
            sum = True
        if self.AND(a, b):
            carry = True
        
        return sum, carry

    def full_add(self, a, b, cin):
        sum1, carry1 = self.half_add(a, b)
        sum2, carry2 = self.half_add(sum1, cin)

        cout = self.OR(carry1, carry2)
        
        return sum2, cout

    def add(self, a, b, cin):
        carry = cin
        cout = False
        result = []

        for i in range(self.bit_len -1, -1, -1):
            sum, carry = self.full_add(a[i], b[i], carry)
            result.append(sum)

        result.reverse()
        if carry:
            cout = carry

        return result, cout

    def subtract(self, a, b):
        sub, cout = self.add(a, self.get_inverse(b), True)
        return sub, cout

    def shift(self, mode, a):
        result = []
        carry = False

        match mode:
            case "0001":
                result, carry = self.shift_left(a)
            case "0010":
                result = self.shift_right(a)

        return result, carry
    
    def shift_left(self, a):
        result, carry = self.add(a, a, False)
        return result, carry

    def shift_right(self, a):
        result = [False] * self.bit_len

        for i in range(1, self.bit_len):
            result[i] = a[i -1]
        return result

    def bitwise_op(self, a, b, operation):
        result = []

        for i in range(self.bit_len):
            result.append(operation(a[i], b[i]))

        return result

    def compare(self, a, b):
        _, flags = self.subtract(a, b)
        return None, flags


    def operate(self, operation, dest, src1, src2):
        result = []
        carry = False

        match operation:
                case "ADD":
                    result, carry = self.add(src1, src2, False)
                case "SUB":
                    result, carry = self.subtract(src1, src2)
                case "OR":
                    result = self.bitwise_op(src1, src2, self.OR)
                case "AND":
                    result = self.bitwise_op(src1, src2, self.AND)
                case "XOR":
                    result = self.bitwise_op(src1, src2, self.XOR)
                case "SFT":
                    result, carry = self.shift(src1, src2)
                case "CMP":
                    _, flags = self.compare(src1, src2)
                case "NOT":
                    result = self.NOT(dest, src1)
                case _:
                    raise SyntaxError(operation + " is not a valid ALU operation.")

        self.reg_file.write(dest, result)

        flags = {
            "Z": not any(result),
            "C": carry
        }
            
        return result, flags





