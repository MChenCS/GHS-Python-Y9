def calculate_sailing_price():
    """Calculates and displays the price payable for sailing tickets, including vehicle fees, night sailing surcharge, and cabin costs, in the user's preferred currency."""

    base_fare_gbp = 60
    ticket_classes = {
        "Economy": 1.0,
        "Flexi": 1.1,
        "Premium": 1.35,
    }
    currency_rates = {
        "GBP": 1.0,
        "EUR": 1.2,
    }
    vehicle_fees = {
        "Small": 100,
        "Large": 200,
    }
    night_sailing_surcharge = 1.15  # 15% surcharge
    cabin_price_gbp = 50
    cabin_discount = 0.5  # 50% discount

    print("Welcome to our sailing ticket service!")
    print("Available ticket classes:")
    for class_name in ticket_classes:
        print(f"- {class_name}")

    print("\nAvailable directions:")
    print("1. UK to NL")
    print("2. NL to UK")

    while True:
        try:
            direction = int(input("Enter direction (1 for UK to NL, 2 for NL to UK): "))
            if direction not in [1, 2]:
                print("Invalid direction. Please enter 1 or 2.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            num_tickets = int(input("Enter the number of tickets: "))
            if num_tickets <= 0:
                print("Invalid number of tickets. Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        ticket_class = input("Enter the ticket class (Economy, Flexi, Premium): ").capitalize()
        if ticket_class not in ticket_classes:
            print("Invalid ticket class. Please choose from Economy, Flexi, or Premium.")
        else:
            break

    print("\nAvailable currencies:")
    for currency in currency_rates:
        print(f"- {currency}")

    while True:
        preferred_currency = input("Enter your preferred currency (GBP or EUR): ").upper()
        if preferred_currency not in currency_rates:
            print("Invalid currency. Please choose from GBP or EUR.")
        else:
            break

    while True:
        sailing_time = input("Is this a day or night sailing? (day/night): ").lower()
        if sailing_time not in ["day", "night"]:
            print("Invalid sailing time. Please enter 'day' or 'night'.")
        else:
            break

    travel_with_vehicle = input("Are you traveling with a vehicle? (yes/no): ").lower()

    vehicle_total_fee_gbp = 0
    if travel_with_vehicle == "yes":
        while True:
            vehicle_type = input("Enter vehicle type (Small/Large): ").capitalize()
            if vehicle_type not in vehicle_fees:
                print("Invalid vehicle type. Please choose from Small or Large.")
            else:
                break
        while True:
            try:
                num_vehicles = int(input("Enter the number of vehicles: "))
                if num_vehicles <= 0:
                    print("Invalid number of vehicles. Please enter a positive number.")
                elif num_vehicles > num_tickets:
                    print("The number of vehicles cannot exceed the number of tickets.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        vehicle_total_fee_gbp = vehicle_fees[vehicle_type] * num_vehicles

    multiplier = ticket_classes[ticket_class]
    ticket_price_gbp = base_fare_gbp * multiplier * num_tickets
    if sailing_time == "night":
        ticket_price_gbp *= night_sailing_surcharge

    cabin_total_fee_gbp = 0
    if sailing_time == "day":
        print("\nCabin options (Day sailing):")
        print("0. Skip cabin selection")
        print("1. Add a basic cabin (max 2)")
        while True:
            try:
                cabin_choice = int(input("Enter cabin choice (0 or 1): "))
                if cabin_choice not in [0, 1]:
                    print("Invalid cabin choice. Please enter 0 or 1.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        if cabin_choice == 1:
            cabin_total_fee_gbp = cabin_price_gbp * cabin_discount
    else:  # Night sailing
        print("\nCabin options (Night sailing):")
        print("1. Add a basic cabin (max 2)")
        while True:
            try:
                num_cabins = int(input(f"Enter the number of cabins (minimum {num_tickets / 2}): "))
                if num_cabins * 2 < num_tickets:
                    print(f"Not enough beds. You need at least {num_tickets / 2} cabins.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        cabin_total_fee_gbp = cabin_price_gbp * num_cabins

    total_price_gbp = ticket_price_gbp + vehicle_total_fee_gbp + cabin_total_fee_gbp
    total_price_preferred = total_price_gbp * currency_rates[preferred_currency]

    print(f"\nPrice for {num_tickets} {ticket_class} ticket(s) is: {total_price_preferred:.2f} {preferred_currency}")
    
calculate_sailing_price()