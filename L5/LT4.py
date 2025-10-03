SALOON_PRICE = 35
SUV_PRICE = 55
MINIVAN_PRICE = 70

car_type = input("What type of car do you want? (Saloon/SUV/Minivan) ")
rental_days = int(input("How many days do you want to rent the car for? "))
if car_type == "Saloon":
    total_cost = SALOON_PRICE * rental_days
elif car_type == "SUV":
    total_cost = SUV_PRICE * rental_days
elif car_type == "Minivan":
    total_cost = MINIVAN_PRICE * rental_days
else:
    total_cost = 0
    print("Invalid car type selected.")
print("The total cost is ", total_cost)