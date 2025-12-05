distance = float(input("Enter distance: "))
fuel_efficiency = float(input("Enter miles_per_gallon: "))
price_per_gallon = float(input("Enter price_per_gallon: "))

price = (distance * price_per_gallon)/fuel_efficiency
print("cost of trip is $" + str(price))
