current_num = float(input("Enter a positive number: "))
total = 0
largest_num = 0
smallest_num = 0

while current_num != 0:
    if current_num < 0:
        print("Number not valid. Please retry")
    else:
        if total == 0:
            largest_num = current_num
            smallest_num = current_num
        else:
            if current_num > largest_num:
                largest_num = current_num
            if current_num < smallest_num:
                smallest_num = current_num
        total += current_num
        print("Number added")
    current_num = float(input("Enter another positive number or 0 to finish: "))

print("Total: ", total)
print("Largest: ", largest_num)
print("Smallest: ", smallest_num)
