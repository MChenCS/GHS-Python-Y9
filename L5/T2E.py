"""
Museum entry - Extra
"""

age = int(input("How old are you? "))
if age < 5:
    price = 0
elif age > 16:
    price = 5
else:
    price = 3
print("You'll need to pay £", price)