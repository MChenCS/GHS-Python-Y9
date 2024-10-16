"""
Debug sleep calculator code
Calculate sleep time per week, month, year & convert such to day
"""

hourspernight = float(input("How many hours per night do you sleep? "))
hoursperweek = hourspernight * 7
print ("You sleep",hoursperweek,"hours per week")

hourspermonth = hourspernight * 30
print ("You sleep",hourspermonth,"hours per month")

hoursperyear = hourspernight * 365
print ("You sleep",hoursperyear,"hours per year")

totaldays = hoursperyear / 24
print("That's equivalent to ", totaldays, " per year!")