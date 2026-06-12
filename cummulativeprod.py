l=list(map(int,input().split()))
p=1
l1=[]
for i in l:
    p*=i
    l1.append(p)
print(l1)