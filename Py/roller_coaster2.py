#Roller coaster

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 44 and age <= 55 :
    print("Your ride is free")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wanna_pic = input(f"Do you want a pic ? ")
  if wanna_pic == "Y" : 
    bill += 3
 

  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller")