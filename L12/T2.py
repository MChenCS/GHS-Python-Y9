def hangman_display(chosen_word, unguessed_word):
    for char in chosen_word:
        if char in unguessed_word:
            chosen_word = chosen_word.replace(char, "_")
    print(chosen_word)

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
    hangman_display(chosen_word, temp)
    
    if temp == "":
        break

if temp == "":
    print("You won!")
else:
    print("You lose")