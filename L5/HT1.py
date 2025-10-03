ARENA_PRICE = 100
STALLS_PRICE = 80
GRAND_TIER_PRICE = 55
SECOND_TIER_PRICE = 35

seat_type = input("What type of seat do you want? (Arena/Stalls/Grand Tier/Second Tier) ")
ticket_count = int(input("How many tickets do you want to buy? "))
ticket_type = input("Which type of ticket do you want? (Non-Refundable/Refundable) ")

if seat_type == "Arena":
    total_cost = ARENA_PRICE * ticket_count
elif seat_type == "Stalls":
    total_cost = STALLS_PRICE * ticket_count
elif seat_type == "Grand Tier":
    total_cost = GRAND_TIER_PRICE * ticket_count
elif seat_type == "Second Tier":
    total_cost = SECOND_TIER_PRICE * ticket_count
else:
    total_cost = 0
    print("Invalid seat type selected.")

if ticket_type == "Non-Refundable":
    total_cost = 0.8 * total_cost

print("The total cost is ", total_cost)