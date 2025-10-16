PASSWORD = "61016"

pwd_attempt = input("What's the password?")
while pwd_attempt != PASSWORD:
    print("Incorrect password. Try again.")
    pwd_attempt = input("What's the password?")

if pwd_attempt == PASSWORD:
    print("You've logged in")