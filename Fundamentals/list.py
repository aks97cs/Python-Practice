'''
Expolring list
'''l =[]
p =[]
for i in range(1,3):
    for j in range(1,3):
        a = input("enter number")
        p.append(a)
    l.append(p)
print(l)
print(l[0][0])
col = [row[1] for row in l] #finding column 2 value
print(col)