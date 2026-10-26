###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    total = 0

    for digit in number:
        total += int(digit)

    return total

number = str(input('Enter integer number: '))

print(f'The sum of the digits in the number {number} is', sum_digits(number))