size = input("What size pizza do you want? S, M, or L ")

add_pepperoni = input("Do you want pepperoni? Y or N ")

peppe_size = input("Do you want pepperoni for Med or large - Med or larg ")
 
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "L" :
    bill = 25
elif size =="M" :
    bill = 20
else : 
    bill = 15
    


if add_pepperoni == "Y" :
    if peppe_size =="L" :
        bill += 
    bill = bill + 5
elif add_pepperoni == "M" :
    bill = bill + 3

if extra_cheese == "Y" :
    bill = bill + 1
    
    print(bill)