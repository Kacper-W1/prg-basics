###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

volume = a * b * c
surface_area = (a * b) * 2 + (a * c) * 2 + (b * c) * 2

print("Volume =", volume)
print("Surface area =", surface_area)