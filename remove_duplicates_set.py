l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
if len(l)==len(l1):
    print("list is unique")
else:
    print("list is not unique")