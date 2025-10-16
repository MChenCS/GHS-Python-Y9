current_num = float(input("Enter a positive number: "))
total = 0

while current_num != 0:
    if current_num < 0:
        print("Number not valid. Please retry")
    else:
        total += current_num
        print("Number added")
    current_num = float(input("Enter another positive number or 0 to finish: "))

print("Total: ", total)