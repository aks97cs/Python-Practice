'''
    @created By: ANuj Kumar Singh
    @code to check whether a number is armstron number or not
    @153 is a armstrong number 

'''
sum = 0
num1 = int(input('Enter the  number: '))
num = num1
while num>0:
    r=num%10
    num=num-r
    num=num/10
    sum = sum+r*r*r
if int(sum) == num1:print('is armstrong')
print(sum,num1)