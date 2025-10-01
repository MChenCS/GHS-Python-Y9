COFFEE_PRICE = 3
TEA_PRICE = 2

print("Do you want coffee or tea?")
drink = input()
if drink == "coffee":
    price = COFFEE_PRICE
else:
    price = TEA_PRICE

print("That will be £",price)