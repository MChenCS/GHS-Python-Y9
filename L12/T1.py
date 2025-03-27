import random

wordlist = ["apple", "cocoa", "coach", "print"]
chosen_word = random.choice(wordlist)
temp = chosen_word

lives = 8

while lives != 0:
    print("You have", lives, "lives left.")
    user_char = input("What character are you guessing? ")
    if user_char in chosen_word:
        print("Right")
        temp = temp.replace(user_char, "")
    else:
        print("Wrong")
    lives = lives - 1
    
    if temp == "":
        break

if temp == "":
    print("You won!")
else:
    print("You lose")