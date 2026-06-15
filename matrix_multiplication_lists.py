m1=[]
m2=[]
m=int(input())
for i in range(m):
    l=list(map(int,input().split()))
    m1.append(l)
for i in range(m):
    l=list(map(int,input().split()))
    m2.append(l)
m3=[]
for i in range(m):
    l=[]
    for j in range(m):
        s=0
        for k in range(m):
            s=s+m1[i][k]*m2[k][j]
        l.append(s)
    m3.append(l)
for row in m3:
    print(*row)