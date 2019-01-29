'''
	created by: Anuj Kumar Singh
	Bubble Sort
	Time Complexity : O(n*n)
'''
l = list()
len = int(input("Enter the length of list : "))
for x in range(0,len):
	l.append(int(input("Enter the element")))
print(l)
for i in range(0,len):
	ptr = i
	for j in range(ptr+1,len):
		if l[ptr]>l[j]:
			l[ptr],l[j] = l[j],l[ptr]

print(l)