"""
Currency converter
"""

GBPEUR = 1.19
GBPUSD = 1.30
GBPJPY = 195

GBPValue = float(input("How much money do you have in GBP?"))

print("We can convert to...")
print("1. EUR")
print("2. USD")
print("3. JPY")
option = input("Which currency?")

if option == "1":
    print("You've chosen EUR")
    foreignValue = GBPValue * GBPEUR
elif option == "2":
    print("You've chosen USD")
    foreignValue = GBPValue * GBPUSD
elif option == "3":
    print("You've chosen JPY")
    foreignValue = GBPValue * GBPJPY
else:
    foreignValue = 0

print("You will receive ", foreignValue, " in your chosen currency.")