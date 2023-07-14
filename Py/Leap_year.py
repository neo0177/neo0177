# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.
# on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)

year = int(input("Which year do you want to check? "))
if year % 4 == 0: 
    print("Leap year.") 
    if (year % 100 == 0) and (year % 400 == 0) :
        print("Leap year.")
        if year % 400 == 0:
            print("Leap year.")
        else:        
            print("Leap year.")
else:
    print("Not Leap year.") 




