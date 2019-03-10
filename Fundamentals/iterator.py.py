'''
    iterator is faster than readlines
    it give speed aprrox to c
'''
#iterator in file
f = open('abc.txt')
print(f.__next__())
l = [1,2,3,4,5]

#iterator in list
I = iter(l)
print(I.__next__())