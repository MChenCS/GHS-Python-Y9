"""
Display hotel prices & availability
"""

dsi_rooms = {
    "single": [8, 60],
    "double": [10, 75],
    "suite": [2, 105]
}

print("Welcome to Diddly Squat Inn!")
for k, v in dsi_rooms.items():
    room_type = k
    room_available = v[0]
    room_price = v[1]
    print("We have ", room_available, room_type, " available at the cost of £", room_price, " each.")