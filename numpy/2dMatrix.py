import numpy as np
a = np.array([[1,2,3],[2,3,4],[3,4,5]])
print("2D Matrix => ")
print(a)
#Traversing each element of 2D Matrix
for i in a:
    for j in i:
        print(j)