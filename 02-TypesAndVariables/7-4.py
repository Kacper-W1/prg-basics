circumference = int(input("Enter tree circumference in cm: "))

r = circumference / 2 / 3.14
diameter = 2 * r

print(f"Tree can be cut down: {diameter >= 50}")