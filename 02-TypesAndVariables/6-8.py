###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')

number_of_letters = ord(last) - ord(first) - 1

print(f'Between {first} and {last} is {number_of_letters} letters')