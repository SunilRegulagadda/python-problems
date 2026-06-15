n = int(input())
d={}
for i in range(n):
    x,y=input().split()
    d[x]=y
k=input()
print(d[k])