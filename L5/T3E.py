"""
Exam grader - Extra
"""

mark = int(input("Enter student's mark:"))
if mark > 49:
    if mark > 60:
        print("P+")
    else:
        print("Pass")
else:
    print("Fail")