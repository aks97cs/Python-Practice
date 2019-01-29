'''
	created by: Anuj Kumar Singh
	Selection Sort Algotithm 
	Time complexibility : O(n*n)
'''
a = list()
len = int(input("How many number you want to insert"))
for i in range(0,len):
	a.append(input("Enter the element :"))
print(a)
for x in range(0,len):
	for y in range(x+1,len):
		if int(a[x])>int(a[y]):
			a[x],a[y] = a[y],a[x]
print(a)