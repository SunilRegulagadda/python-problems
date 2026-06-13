l=list(map(int,input().split()))
l1=[]
for i in range(1,len(l)):
    l1.append(l[i-1]-l[i])
print(l1)