def calculate_sailing_price():
    """Calculates and displays the price payable for sailing tickets."""

    base_fare = 60
    ticket_classes = {
        "Economy": 1.0,
        "Flexi": 1.1,
        "Premium": 1.35,
    }

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

    multiplier = ticket_classes[ticket_class]
    total_price = base_fare * multiplier * num_tickets

    print(f"\nPrice for {num_tickets} {ticket_class} ticket(s) is: £{total_price:.2f}")

calculate_sailing_price()