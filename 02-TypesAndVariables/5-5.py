price = float(input("Enter price: "))
discount = float(input("Enter discount in %: "))

discounted_price = round(price * ((100 - discount) / 100), 2)
difference = round(price - discounted_price, 2)

print("Price with discount:", discounted_price)
print("Reduction:", difference)