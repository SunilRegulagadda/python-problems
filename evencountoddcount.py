n=int(input("enter number of elements"))
l=[]
for i in range(n):
    l.append(int(input()))
evenc=0
oddc=0
for i in l:
    if i%2==0:
        evenc+=1
    else:
        oddc+=1
print(evenc,oddc)