# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = name1 + name2
print(type(combined_name))

lower_name = combined_name.lower()
print(type(lower_name))

print(lower_name)
t = lower_name.count("t")
print(t)
r = lower_name.count("r")
print(r)
u = lower_name.count("u")
print(u)
e = lower_name.count("e")
print(e)

true_num = int(t + r + u + e)
print(true_num)

l = lower_name.count("l")
print(l)
o = lower_name.count("o")
print(o)
v = lower_name.count("")
print(v)
e = lower_name.count("e")
print(e)

love_num = int(t + r + u + e)
print(love_num)

score = true_num + love_num

print(type(score))

if (score < 10 ) or (score > 90 ):
    print(f"Your score is {love_strength}, you go together as Mentos and coke")

elif (score < 10 ) or (score > 90 ):
    print(f"Your score is {love_strength}, you go together as Mentos and coke")
