"""
Set and check password
"""

pwd = input("Set a password: ")

attempt = input("Enter the password: ")
if pwd == attempt:
    print("Correct. Phone unlocked")
else:
    print("Wrong password")