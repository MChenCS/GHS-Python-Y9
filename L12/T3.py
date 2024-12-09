def wordle_display(user_word_list, temp_list):
    print("You've guesed:")
    print(list_to_string(user_word_list, True))
    print(list_to_string(temp_list, True))
    print("A character means you've guessed the correct character at the correct position,")
    print("A star means you've guessed the correct character but at the incorrect position,")
    print("A underline means you've guessed the incorrect character.")

def list_to_string(phrase, space):
    return_string = ""
    if space:
        for elem in phrase:
            return_string = return_string + elem + " "
    else:
        for elem in phrase:
            return_string = return_string + elem
    return return_string

import random

wordlist = ["apple", "cocoa", "coach", "print"]
chosen_word = random.choice(wordlist)
temp = chosen_word

lives = 8

while lives != 0:
    print("You have", lives, "lives left.")
    user_word = input("What word are you guessing? ")
    
    user_word_list = list(user_word)
    chosen_word_list = list(chosen_word)
    temp = chosen_word
    temp_list = list(temp)

    if user_word_list == chosen_word_list:
        break

    for i in range(len(chosen_word)):
        if user_word_list[i] in chosen_word_list: # Yellow only
            if user_word_list[i] == chosen_word_list[i]: # Yellow and green
                temp_list[i] = user_word_list[i]
            else:
                temp_list[i] = "*"
        else:
            temp_list[i] =  "_"

    wordle_display(user_word_list, temp_list)
    lives = lives - 1

if user_word_list == chosen_word_list:
    print("You won!")
else:
    print("You lost")