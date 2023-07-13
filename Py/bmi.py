# weight = 0
# height = 0

# # bmi = (weight(kg)) / height**2(m**2)

# weight_integer = float(input("What is your weight ? "))
# print(type(weight_integer))

# height_integer = float(input("What is your height ? "))
# print(type(height_integer))

# bmi = (weight_integer )/ (height_integer * height_integer)

# print(round(bmi))


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight / height ** height)
print(bmi)


# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")