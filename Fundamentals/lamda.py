'''
    @Created By: Anuj kumar Singh
    @Understanding the concept of lamda
'''
x  = lambda x:x+x
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n