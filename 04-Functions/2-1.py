###
# Program for testing built-in functions
#

max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Enter a letter:")
print("The letter read from the keyboard is", letter)

for char in "20303":
    number = ord(char)

    print(number)

print("The binary representation of decimal number 304 is", bin(304))

print("The hexadecimal representation of decimal number 304 is", hex(304))

print("The integer representing the unicode of the sign € is", ord("€"))

print("The absolute value of -17 is", abs(-17))