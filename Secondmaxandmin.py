l=list(map(int,input().split()))
l.sort()
max=l[-1]
for i in range(len(l)-2-1,-1,-1):
    if l[i]!=max:
        print("Second max is ",l[i])
        break
min=l[0]
for i in range(1,len(l)):
    if l[i]!=min:
        print("Second min is ",l[i])
        break
