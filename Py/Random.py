# import random

# random_int = random.randint(0,1)
# sum = 0

# if random_int == 0:
#     print("Its Head")
    
# else:
#     print(f"You have  Tail")

# answer = input("Would you wanr to try agian ? Y Or N ")

# sum += 1

# print(f"Total number of tries {sum}")
    

# Import the random module here

# Split string method

import random

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(",  ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# num_pay = len(names)

# random_name = random.randint(0, num_pay -1)
# # print(f"the person to pay is {random_name}")
# print(random_name)

# persont_pay = names[random_name]
# print(persont_pay + "will pay hte bil")


names = input("Enter the names with comma ?")

x = names.split()
num_of = len(x)
print(num_of)
print(x)
