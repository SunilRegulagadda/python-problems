n=int(input("Enter the number of elements: "))
a=list(map(int,input("Enter the elements: ").split()))
d={}
for i in a:
    val=d.get(i,0)
    d[i]=val+1
x=max(d.values())
for i in d:
    if d.get(i)==x:
        print(i,":",x)