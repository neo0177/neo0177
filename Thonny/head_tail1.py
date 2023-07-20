# Head & Tail.
# 1. Head   2. Tail
# Input your choice: 1 or 2
# If its head and you choose head, you win
# If its tail and you choose tail, you win
# If its head and you choose tail, you lose
# If its tail and you choose head, you lose
import random
choice = input("Enter your choice 1 'Heads' or 'Tails' ? ")
choice_random = random.randint(1,2)
print(choice_random)
print(choice)

if choice == 1 :
        print("Its a draw") 
else :
    print("You win")