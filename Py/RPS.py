import random
bot = int(input("What would you like to choose : rock ; 1, paper : 2, scissor : 3, and  4: quit ? "))

rand_int = random.randint(1,3)
print(rand_int)



if rand_int == 1 :
    print("Its a tie")
elif ((bot == 1  and rand_int == 2)) or ((bot == 2 and rand_int == 3)) or ((bot == 3 and rand_int == 1)):
    print(" print you win ")
elif bot == 4 :
    print("Game Over")
else:
    print("You loose")



# rock beats scisors, scisors beats paper and paper beats rock