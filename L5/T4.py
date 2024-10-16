"""
Tax calculator
"""

salary = float(input("What's the employee's salary? "))
tax = salary * 0.09
takehomepay = salary - tax
print("You're paying £", tax, " in tax. Your take home pay is £", takehomepay)