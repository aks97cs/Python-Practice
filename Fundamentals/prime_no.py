'''
    @ Created By: Anuj Kumar Singh
    @ Description : code to check whether a number is prime or not
'''
num = int(input("Enter a number"))
flag=0
for i in range(2,round(num/2)):
    if num%i == 0:
        flag = 1
if flag == 0:
    print('Prime number')
else:
    print('Not a prime number')