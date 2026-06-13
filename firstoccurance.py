l=list(map(int,input().split()))
n=int(input("Enter number to find "))
for i in range(len(l)):
    if l[i]==n:
        print(i)
        break
else:
    print(-1)
