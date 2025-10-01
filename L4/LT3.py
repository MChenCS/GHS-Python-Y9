PRICE_PER_SANDWICH = 3

num_sandwich = int(input("Number of sandwiches: "))
if num_sandwich >= 12:
    price = num_sandwich * PRICE_PER_SANDWICH * 0.8
else:
    price = num_sandwich * PRICE_PER_SANDWICH
print("That will be £",price) 