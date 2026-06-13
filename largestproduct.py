l=list(map(int,input().split()))
n=len(l)
p1=0
p2=0
l.sort()
p1=l[0]*l[1]
p2=l[n-1]*l[n-2]
if p1>p2:
    print(p1)
else:
    print(p2)