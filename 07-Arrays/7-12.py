categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

for i in range(0, len(expenses)):
    if expenses[i] == max(expenses):
        print("The most expensive category:", categories[i])