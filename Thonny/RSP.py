import random
# bot = int(input("What would you like to choose : rock ; 1, paper : 2, scissor : 3, and  4: quit ? "))
bot = input("What would you like to choose : rock ; 1, paper : 2, scissor : 3, and  4: quit ? ")

bot = ["rock", "paper", "scissor"]

rand_int = random.choice(bot)
print(rand_int)


if rand_int == "rock" :
    print("Its a tie")
elif ((bot == "rock"  and rand_int == "paper")) or ((bot == "paper" and rand_int == "scissor")) or ((bot == "scissor" and rand_int == "rock")):
    print(" print you win ")
elif bot == 4 :
    print("Game Over")
else:
    print("You loose")
