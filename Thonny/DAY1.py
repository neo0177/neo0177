# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_int = int(weight)
height_float = float(height)


# or using multiplication and PEMDAS
bmi = weight_int / (height_float * height_float)

bmi_as_int = int(bmi)

print(bmi_as_int)