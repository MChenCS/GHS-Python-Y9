membership = input("Are you a member (Y/N)? ")
if membership == "Y":
    book_unit_price = 3.5
else:
    book_unit_price = 4.5

num_books = int(input("Number of books: "))
print("That will be £", num_books * book_unit_price)