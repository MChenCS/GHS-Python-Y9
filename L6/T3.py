"""
Add parking & breakfast
"""

dsi_rooms = {
    "single": [8, 60],
    "double": [10, 75],
    "suite": [2, 105]
}

dsi_addon = {
    "parking": 20,
    "breakfast": 12
}

print("Welcome to Diddly Squat Inn!")
for k, v in dsi_rooms.items():
    room_type = k
    room_available = v[0]
    room_price = v[1]
    print("We have ", room_available, room_type, " available at the cost of £", room_price, " each.")

reservation_room = input("Which room do you want? ").lower()
while reservation_room not in dsi_rooms.keys():
    print("Input not recognised. Please try again.")
    reservation_room = input("Which room do you want? ")
reservation_rate = float(dsi_rooms.get(reservation_room)[1])

reservation_nights = input("How many nights do you want to stay in the room? ")
while not reservation_nights.isnumeric():
    print("Input not recognised. Please try again.")
    reservation_nights = input("How many nights do you want to stay in the room? ")

while int(reservation_nights)<1:
    print("Input not recognised. Please try again.")
    reservation_nights = input("How many nights do you want to stay in the room? ")
reservation_nights = int(reservation_nights)

print("Do you want to add parking? Parking is £", dsi_addon.get("parking"), " extra per day.")
reservation_parking = input("Enter Y or N ")
while not(reservation_parking == "Y" or reservation_parking == "N"):
    print("Input not recognised. Please try again.")
    reservation_parking = input("Do you want to add parking? Enter Y or N ")
if reservation_parking == "Y":
    reservation_parking = True
else:
    reservation_parking = False

print("Do you want to add breakfast? Breakfast is £", dsi_addon.get("breakfast"), " extra per day regardless of number of guests.")
reservation_breakfast = input("Enter Y or N ")
while not(reservation_breakfast == "Y" or reservation_breakfast == "N"):
    print("Input not recognised. Please try again.")
    reservation_breakfast = input("Do you want to add breakfast? Enter Y or N ")
if reservation_breakfast == "Y":
    reservation_breakfast = True
else:
    reservation_breakfast = False

if reservation_parking:
    reservation_rate = reservation_rate + dsi_addon.get("parking")

if reservation_breakfast:
    reservation_rate = reservation_rate + dsi_addon.get("breakfast")

reservation_price = reservation_rate * reservation_nights
print("That would be £", reservation_price)