###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2

    a = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return a

a = int(input("Enter 1st side's length: "))
b = int(input("Enter 2nd side's length: "))
c = int(input("Enter 3rd side's length: "))

area = triangle_area(a, b, c)

print(f'The area of a triangle with sides {a}, {b}, {c} is {area}')