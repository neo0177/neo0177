
year_to_check = int(input("Which year do you want to check? "))
if year_to_check % 4 == 0: 
    print("Leap year.") 
    if (year_to_check % 100 == 0) and (year_to_check % 400 == 0) :
        print("Leap year.")
        if year_to_check % 400 == 0:
            print("Leap year.")
        else:        
            print("Leap year.")
else:
    print("Not Leap year.") 