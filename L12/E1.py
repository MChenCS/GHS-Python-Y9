"""
Using code from:
https://www.andy-pearce.com/blog/posts/2015/Aug/validating-uk-postcodes/
"""
import re

NON_ALPHA_RE = re.compile('[^A-Z0-9]+')
POSTCODE_RE = re.compile('^[A-Z]{1,2}[0-9]{1,2}[A-Z]? [0-9][A-Z]{2}$')

def check_postcode(postcode):
    """check if a given postcode is valid or not"""

    postcode = NON_ALPHA_RE.sub('', postcode.upper())
    postcode = postcode[:-3] + ' ' + postcode[-3:]
    if POSTCODE_RE.match(postcode):
        return True
    return False

def check_local_authority(postcode, local_authority):
    if postcode.startswith(local_authority):
        return True
    else:
        return False
    
def check_age(age):
    if age > 120 or age < 0:
        return 0
    elif age < 18:
        return 1
    else:
        return 2

local_authority = "SM"
candidates = ["Aiden", "Bryan", "Chessie", "Demi", "Elva", "Frannkie"]

voter_valid = False

print("Welcome to local voting!")
print("First, we need to validate your postcode.")
postcode = input("What's your postcode? ")
if check_postcode(postcode):
    if check_local_authority(postcode, local_authority):
        voter_valid = True
    else:
        print("Looks like that you do not live in the local area. You cannot vote here unfortunately.")
else:
    print("We cannot recognise the postcode you've given.")

if voter_valid:
    print("Now we need to check your age.")
    age = int(input("How old are you? "))
    age_result = check_age(age)
    if age_result == 0:
        print("We cannot recognise the age you've given.")
        voter_valid = False
    elif age_result == 1:
        print("Looks like that you're not old enough to vote yet.")
        voter_valid = False

if voter_valid:
    print("Please choose from the following candidates: ")
    print(candidates)
    choice = input("Who is your choice? ")
    if choice not in candidates:
        print("We cannot recognise the choice you've given.")
    else:
        print("Your choice of", choice, "has been registered.")