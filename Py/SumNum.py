#Example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
# 1. Get the number from the user  (input)
# 2. Add all the numbers from 1 to the number (for loop)
# 3. Print the result (print)
number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):
    sum = sum + i
print(sum)
