print("Enter the three number")
num1=input("enter the first number")
num2=input("enter the second number")
num3=input("enter the third number")
num1=int(num1)
num2=int(num2)
num3=int(num3)
if num1>num2:
    if num1>num3:
        print(num1,"is a greatest number")
    else:
        print(num3,"is a greatest value")
else:
    if num2>num3:
        print(num2,"is a greatest number")
    else:
        print(num3,"is a greatest number")
