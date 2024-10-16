"""
Grading
"""
grade = int(input("What's your grade out of 100? "))
if grade >= 80:
    print("Distinction")
elif grade >= 70:
    print("Merit")
elif grade >= 60:
    print("Pass")
else:
    print("Fail")