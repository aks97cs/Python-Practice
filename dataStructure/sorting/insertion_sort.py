'''
	Created By: Anuj Kumar Singh
	Insertion Sort Algorithm
	Time Complexity : O(n*n)
'''
l = list()
len = int(input("Enter the lenght of list"))
for x in range(0,len):
	l.append(int(input("Enter the element")))
print(l)
for i in range(0,len-1):
	j=i
	while j>=0:
		if l[j]>l[j+1]:
			l[j],l[j+1] = l[j+1],l[j]
		j = j-1
print(l)