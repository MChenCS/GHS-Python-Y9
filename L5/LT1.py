age = int(input("How old are you?"))
nationality = input("Are you a British national?")
if age >= 18:
    if nationality == "Yes":
        print("You can vote")
    else:
        print("You cannot vote")
else:
    print("Sorry, you cannot vote")
