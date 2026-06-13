l=[100,4,900,1,3,2,9,11,12,10,15,13,16,14]
l.sort()
print(l)
max_count=1
count=1
for i in range(1,len(l)):
    if l[i]==l[i-1]:
        continue
    elif l[i]==l[i-1]+1:
        count+=1
    else:
        max_count=max(max_count,count)
        count=1
max_count=max(max_count,count)
print(max_count)