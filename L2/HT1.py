# Get user information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
year = input("Enter the sign up year: ")

# Extract last 2 digits of year
year_digits = year[-2:]

# Generate ID using the format: [year][surname][first char of first name]
library_id = year_digits+surname+first_name[0]

# Display the ID
print("Your library ID is: ", library_id)