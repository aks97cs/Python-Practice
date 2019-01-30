'''
    @created By: ANuj Kumar Singh
    @understanding the concept of iteraotrs

'''
# data = ("anuj","Ram","shiva","subham","satyam","ayush")
data = "Anuj"
list_data = iter(data)
print(next(list_data))
print(next(list_data))
print(next(list_data))
print(next(list_data))

'''
    to craete an object/class an iterator we need to implement __iter__() and __next__()
'''
class Mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 2
        return x
classObj = Mynumber()
myiter = iter(classObj)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''
    To prevent the iteration to go on forever, we can use the StopIteration statement.
    In the __next__() method, we can add a terminating condition to raise an error 
    if the iteration is done a specified number of times:

'''

