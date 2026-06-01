num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
largest = num1
if num2 > largest and num2 > num3:
    largest = num2
elif num3 > largest and num3 > num2:
    largest = num3
print("The largest number is:", largest)    