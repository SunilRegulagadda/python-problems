d={}
n=int(input("Enter the number of elements: "))
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v
dict1=dict(sorted(d.items(),key=lambda x:x[0]))
dict2=dict(sorted(d.items(),key=lambda x:x[0],reverse=True))
dict3=dict(sorted(d.items(),key=lambda x:x[1]))
dict4=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
print("Original dictionary:", d)
print("Sorted by keys:", dict1)
print("Sorted by keys (descending):", dict2)
print("Sorted by values:", dict3)
print("Sorted by values (descending):", dict4)