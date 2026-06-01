num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    largest = num1 #num2 become largest
    if num2 > num3:
        secondL = num2
    else:
        secondL = num3
elif num2 > num1 and num2 > num3:
    largest = num2 #num2 become largest
    if num1 > num3:
        secondL = num1
    else:
        secondL = num3
else: #now c is largest
    if num1 > num2:
        secondL = num1
    else:
        secondL = num2

print("The second largest number is:", secondL)  