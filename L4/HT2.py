VAT_RATE = 20

option = input("Do you want to add (A) or remove (R) VAT? ")
original_price = float(input("Enter the original price: "))
if option == "A":
    calculated_price = original_price * (1 + VAT_RATE / 100)
else:
    calculated_price = original_price / (1 + VAT_RATE / 100)
print("The calculated price is £", calculated_price)