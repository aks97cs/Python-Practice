'''
Created By: Anuj Kumar Singh
Code code to find sum of n digit number

'''
num = int(input('Enter the Number:'))
sum = 0
while num>0:
    r=num%10
    sum+=r
    num = num-r
    num = num/10
print("sum = ",sum)
