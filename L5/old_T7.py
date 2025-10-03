"""
Air Luggage
"""

prohibited = input("Do you have any restricted items in your luggage?")
if prohibited.lower() == "no":
    weight = float(input("How much does your luggage weigh?"))
    if weight < 22:
        print("It's allowed")
    else:
        print("We cannot check this for you.")
else:
    print("We cannot check this for you.")