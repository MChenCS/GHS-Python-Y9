# Set the price per can
PRICE_PER_CAN = 2.00

# Ask user for quantity
quantity = int(input("How many cans of sparkling water do you want? "))

# Calculate total cost
total_cost = PRICE_PER_CAN * quantity

# Display result
print("Total amount payable: £", total_cost)