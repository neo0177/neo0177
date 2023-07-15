#Make a rigth angle triangle with the given number of rows.
#Example, if the user entered 5 the output should be:
#
# 1. Get the number from the user  (input)  
# 2. Print the result (print)
# 3. Add a star to the string (concatenation)
# 4. Print the string (print)
# 5. Repeat steps 3 and 4 until the number of rows is reached (for loop)
number = int(input("Enter a number: "))
star = "*"
for i in range(1, number + 1):
    print(star)
    star = star + " *"  # star += " *"
    