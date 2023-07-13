

print("Welcome to the Tip Calculator !!!!!!!")
bill = float(input("HWhat is the Total Bill  ?  "))

print(type(bill))

friend_num = int(input(" How many friends to share with ??  "))
print(type(friend_num))

tip = int(input("How much percentage tip  10,15, 20 percentage ???  "))
print(type(tip))

total_bill = round((tip / 100) * bill + bill)
print(type(total_bill)), 2 

                    
print( " amount each friend is " + total_bill)











