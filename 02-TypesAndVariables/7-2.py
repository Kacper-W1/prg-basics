###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
print(f'Password length is valid: {len(password) >= 8}')