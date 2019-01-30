'''
    @Created By:Anu Kumar Singh
    @code to check whether a number is pallindrom or not
'''
num = int(input('Enter the number'))
l =  list() # for list
r = 0 # for storing remender
flag =0 # to apply check
while num>0:
    r = num%10
    l.append(int(r))
    num=num-r
    num=num/10
j = len(l)
for i in range(0,len(l)):
    if l[i]!=l[j-1]:
        print(l[i],'i=',i)
        print(l[j-1],'j=',j)
        flag=1
    j = j-1
print('is pallindrom') if flag == 0 else print('not a pallindrom')