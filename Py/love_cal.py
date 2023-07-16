#You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

print('Welcome to the "Love Calculator" !!!!!!!')
name1 = input("What is your name? \n")  #input name1        
name2 = input("What is their name? \n") #input name2
name1 = name1.lower() #convert name1 to lower case
name2 = name2.lower() #convert name2 to lower case

t = name1.count('t') + name2.count('t') #count the number of 't' in name1 and name2
r = name1.count('r') + name2.count('r') #count the number of 'r' in name1 and name2     
u = name1.count('u') + name2.count('u') #count the number of 'u' in name1 and name2
e = name1.count('e') + name2.count('e') #count the number of 'e' in name1 and name2
true = t + r + u + e #add the number of 't', 'r', 'u', 'e' in name1 and name2   

l = name1.count('l') + name2.count('l') #count the number of 'l' in name1 and name2
o = name1.count('o') + name2.count('o') #count the number of 'o' in name1 and name2
v = name1.count('v') + name2.count('v') #count the number of 'v' in name1 and name2
e = name1.count('e') + name2.count('e') #count the number of 'e' in name1 and name2
love = l + o + v + e #add the number of 'l', 'o', 'v', 'e' in name1 and name2

love_score = int(str(true) + str(love)) #combine the number of 'true' and 'love' to make a 2 digit number
print(f"Your love score is {love_score}.")