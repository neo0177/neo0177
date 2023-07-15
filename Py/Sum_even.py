#Sum of even numbers in a range.
num = int(input("Enter a number: "))
sum = 1
for i in range(1, num + 1):
    if i % 2 == 0:
        sum = sum + 0
    print(sum)
