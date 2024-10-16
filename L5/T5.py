"""
Service charge
"""

bill = float(input("What's the total bill price?"))

if bill > 100:
    svcChrage = 0
else:
    svcChrage = 100 * bill

print("Your service charge is", svcChrage)