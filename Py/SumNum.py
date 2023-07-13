#Example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

number = int(input("Please enter the number ? "))
total_sum = sum(range(1,number+1))
print(type(total_sum))
print(total_sum)

i = 0
for num in number :
    i += num
    print(i)
