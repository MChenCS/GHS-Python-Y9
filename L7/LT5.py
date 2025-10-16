PASSWORD = "61016"
MAX_ATTEMPTS = 5 
attempts = 0

pwd_attempt = input("What's the password?")
while pwd_attempt != PASSWORD:
    if attempts == MAX_ATTEMPTS:
        print("You've been locked out")
        break
    print("Incorrect password. Try again.")
    attempts +=1
    pwd_attempt = input("What's the password?")

if pwd_attempt == PASSWORD:
    print("You've logged in")