#!/usr/bin/env python3

def calculate_sailing_price():
	"""Calculates and displays the price payable for sailing tickets, including vehicle fees, night sailing surcharge, cabin costs, return journey discount, and connecting train tickets, in the user's preferred currency."""
	
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
	cabin_prices_gbp = {
		"Inside": 50,
		"Outside": 65,
		"Family": 100,
		"Comfort": 130,
		"Suite": 165,
	}
	cabin_capacities = {
		"Inside": 2,
		"Outside": 2,
		"Family": 5,
		"Comfort": 2,
		"Suite": 2,
	}
	return_discount = 0.8  # 20% discount
	uk_train_price_gbp = 7.50
	nl_train_price_gbp = 6.50
	both_trains_discount_gbp = 3.00
	
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
		
	return_journey = input("Is this a return journey? (yes/no): ").lower()
	
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
		if return_journey == "yes":
			vehicle_total_fee_gbp *= return_discount
			
	multiplier = ticket_classes[ticket_class]
	ticket_price_gbp = base_fare_gbp * multiplier * num_tickets
	if sailing_time == "night":
		ticket_price_gbp *= night_sailing_surcharge
	if return_journey == "yes":
		ticket_price_gbp *= return_discount
		
	cabin_total_fee_gbp = 0
	if sailing_time == "day":
		print("\nCabin options (Day sailing):")
		print("0. Skip cabin selection")
		for i, cabin_type in enumerate(cabin_prices_gbp):
			print(f"{i + 1}. Add {cabin_type} cabin (max {cabin_capacities[cabin_type]})")
		while True:
			try:
				cabin_choice = int(input(f"Enter cabin choice (0-{len(cabin_prices_gbp)}): "))
				if cabin_choice < 0 or cabin_choice > len(cabin_prices_gbp):
					print(f"Invalid cabin choice. Please enter a number between 0 and {len(cabin_prices_gbp)}.")
				else:
					break
			except ValueError:
				print("Invalid input. Please enter a number.")
		if cabin_choice != 0:
			selected_cabin = list(cabin_prices_gbp.keys())[cabin_choice - 1]
			cabin_total_fee_gbp = cabin_prices_gbp[selected_cabin]
	else:  # Night sailing
		print("\nCabin options (Night sailing):")
		for i, cabin_type in enumerate(cabin_prices_gbp):
			print(f"{i + 1}. Add {cabin_type} cabin (max {cabin_capacities[cabin_type]})")
		while True:
			try:
				cabin_choice = int(input(f"Enter cabin choice (1-{len(cabin_prices_gbp)}): "))
				if cabin_choice < 1 or cabin_choice > len(cabin_prices_gbp):
					print(f"Invalid cabin choice. Please enter a number between 1 and {len(cabin_prices_gbp)}.")
				else:
					break
			except ValueError:
				print("Invalid input. Please enter a number.")
		selected_cabin = list(cabin_prices_gbp.keys())[cabin_choice - 1]
		while True:
			try:
				num_cabins = int(input(f"Enter the number of {selected_cabin} cabins (minimum {num_tickets / cabin_capacities[selected_cabin]}): "))
				if num_cabins * cabin_capacities[selected_cabin] < num_tickets:
					print(f"Not enough beds. You need at least {num_tickets / cabin_capacities[selected_cabin]} cabins.")
				else:
					break
			except ValueError:
				print("Invalid input. Please enter a number.")
		cabin_total_fee_gbp = cabin_prices_gbp[selected_cabin] * num_cabins
	
	train_total_fee_gbp = 0
	if travel_with_vehicle == "no":
		uk_train = input("Do you want to purchase a UK train ticket? (yes/no): ").lower()
		nl_train = input("Do you want to purchase a Netherlands train ticket? (yes/no): ").lower()
		
		if uk_train == "yes" and nl_train == "yes":
			train_total_fee_gbp = (uk_train_price_gbp + nl_train_price_gbp - both_trains_discount_gbp)
		elif uk_train == "yes":
			train_total_fee_gbp = uk_train_price_gbp
		elif nl_train == "yes":
			train_total_fee_gbp = nl_train_price_gbp
			
	total_price_gbp = ticket_price_gbp + vehicle_total_fee_gbp + cabin_total_fee_gbp + train_total_fee_gbp
	total_price_preferred = total_price_gbp * currency_rates[preferred_currency]
	
	print(f"\nPrice for {num_tickets} {ticket_class} ticket(s) is: {total_price_preferred:.2f} {preferred_currency}")
	
calculate_sailing_price()