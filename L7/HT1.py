import random
MAX_ATTEMPTS = 7

rand_num = random.randint(1,100)
attempts = 0
guess = int(input("Guess a number: "))
while guess != rand_num:
    if attempts == MAX_ATTEMPTS:
        print("You've run out of chances")
        break
    if guess < rand_num:
        print("Too small")
    elif guess > rand_num:
        print("Too large")
    attempts += 1
    guess = int(input("Guess another number: "))

if guess == rand_num:
    print("Spot on!")
    print("It took you ", attempts, " attempts.")