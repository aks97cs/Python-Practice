import numpy as np
height  = np.array([1,2,3,4,5])
print(height**2)
print(height+height)
print(np.array([1,2,3,4,5])+height)
print(type(height))
print(height[0])
numpy_2d = np.array([[1,2,3],[3,4,5]])
print(numpy_2d)
print("index  value of numpy_2d = ",numpy_2d[0])
print(numpy_2d.shape)
''' 
    @subsetting...
'''
print("subsetting data - ",numpy_2d[:,1:3])
print("===>",numpy_2d[1,:])
print("average = ",np.mean(numpy_2d[0,:])) # finding average from row and column 