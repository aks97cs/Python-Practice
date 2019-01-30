def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(5))
'''
    Recursive fabnaci series
'''
def feb(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n>1:
        return feb(n-2)+feb(n-1)
# print(feb(10))
num =10
for i in range(num):
    print(feb(i))