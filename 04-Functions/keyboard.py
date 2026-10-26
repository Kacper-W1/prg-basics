###
# Functions to read any data type from the keyboard
#
def input_string(message):
    string = input(message)
    return string

def input_integer(message):
    int = int(input(message))
    return int

def input_real(message):
    real = float(input(message))
    return real

def input_boolean(message):
    if message == "y":
        boolean = 1
    elif message == "n":
        boolean = 0
    return boolean