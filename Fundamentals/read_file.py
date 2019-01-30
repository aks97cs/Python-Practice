'''
    @Created By:Anuj Kumar Singh
    @working on file handaling

'''
f = open('test.txt',"rt")
# print(f.read())

# read only part of file 
# print(f.read(5))

#reading line 
# print(f.readline())
# print(f.readline())
# print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line:

for x in f:
    print(x)
    # break
