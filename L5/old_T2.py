"""
Museum entry
"""

age = int(input("How old are you? "))
if age < 5:
    price = 0
else:
    price = 3
print("You'll need to pay £", price)