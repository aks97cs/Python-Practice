'''
    Created By: Anuj Kumar Singh
    Merge Sort Algorithm 
    Time Complexity : O(log n)
'''
l = list()
len = int(input("Enter the length of list"))
for i in range(0,len):
    l.append(int(input("Enter the element")))
# def merge(p=0,q=len):
#     n1 =  

def merge_sort(p,r):
    if p<r:
        print("*************************************************")
        q = (p+r)/2
        merge_sort(p,q)
        merge_sort(q+1,r)
merge_sort(0,len-1)
