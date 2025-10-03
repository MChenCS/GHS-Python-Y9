"""
Tax calculator - Extra
"""

salary = float(input("What's the employee's salary? "))
if salary < 100:
    tax = salary * 0.09
else:
    tax = 100 * 0.09 + (salary - 100) * 0.12
takehomepay = salary - tax
print("You're paying £", tax, " in tax. Your take home pay is £", takehomepay)