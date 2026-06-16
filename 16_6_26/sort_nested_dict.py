n=int(input("Enter the number of elements: "))
d={}
for i in range(n):
    k=input("Enter key: ")
    d1={}
    n1=int(input("Enter the number of nested elements: "))
    for i in range(n1):
        k1,v1=map(str,input("Enter nested key and value: ").split())
        d1[k1]=v1
    d[k]=d1
dict1=dict(sorted(d.items(),key=lambda x:(x[0][0],x[0][1])))
print("Original dictionary:", d)
print("Sorted by keys:", dict1)