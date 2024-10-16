"""
Check speed of vehicle
"""

speed = float(input("What's the speed of your car?"))
if speed < 30:
    print("You're fine")
elif speed <40:
    print("Here's a warning. Slow down")
else:
    print("Get ready to receive a ticket")