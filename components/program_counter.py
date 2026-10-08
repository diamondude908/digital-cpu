prog_len = 0
counter = 0

def get():
    return counter

def increment():
    global counter
    counter += 1

def jump(address):
    global counter
    counter = address