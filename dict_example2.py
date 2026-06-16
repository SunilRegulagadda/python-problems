n=int(input())
d={}
for i in range(n):
    x,y=input().split()
    d[x]=int(y)
k=input()
print(d[k])
l=d.values()
a=max(l)
for i in d:
    if d[i]==a:
        print(i)
