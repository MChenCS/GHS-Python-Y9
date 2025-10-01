"""
Caluclate phone bill
"""

name = input("Hello, what's your name?")
network = input("Are you with EE, O2, Vodafone or Three?")
minutes = float(input("How many minutes did you spend on telephone calls over the past month?"))
callCost = minutes * 0.10
text = int(input("How many text messages did you send over the past month?"))
textCost = text * 0.05

totalBill = callCost + textCost
print("Your total bill with ", network, " before VAT is ", totalBill)
print("Your total bill with ", network, " after VAT is ", totalBill * 1.2)