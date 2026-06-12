l=[]
n=int(input())
for i in range(n):
    l1=list(map(str,input().split()))
    l.append(l1)
print("1 sort by emp name")
print("2 sort by emp job")
print("3 sort by emp salary")
print("4 sort by location")
print("5 sort by grade")
print("6 job and salary")
print("7 grade and job")
print("8 grade ,salary and location")
print("9 exit")

while True:
    c=int(input())
    match c:
        case 1:
            l.sort(key=lambda x:x[0])
            print(l)
        case 2:
            l.sort(key=lambda x:x[1])
            print(l)
        case 3:
            l.sort(key=lambda x:x[2])
            print(l)
        case 4:
            l.sort(key=lambda x:x[3])
            print(l)
        case 5:
            l.sort(key=lambda x: (x[4]))
            print(l)
        case 6:
            l.sort(key=lambda x: (x[1], x[2]))
            print(l)
        case 7:
            l.sort(key=lambda x: (x[4], x[1]))
            print(l)
        case 8:
            l.sort(key=lambda x: (x[4], x[2], x[3]))
            print(l)
        case 9:
            break
        case _:
            print("invalid choice")





            