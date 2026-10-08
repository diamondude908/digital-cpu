
def binary(value):
    return [c == "1" for c in value]

def one_bin(value):
    return value == "1"

def display_bin(bits):
    if bits is None:
        return ""
    return "".join("1" if bit else "0" for bit in bits)