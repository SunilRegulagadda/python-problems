def push(n):
    l.append(n)
def pop(l):
    if l==0:
        return none
    else:
        return l.pop()
def top(l):
    if l==0:
        return none
    else:
        return l[-1]
def isEmpty(l):
    if len(l)==0:
        print("stack is empty")
    else:
        print("stack size is",len(l))
def size(l):
    print(len(l))
def display(l):
    print(l)
l=[]
while True:
    print("1. Push")
    print("2. Pop")
    print("3. top")
    print("4. isEmpty")
    print("5. size of stack")
    print("6. Display full stack")
    print("7. Exit")
    c=int(input("Enter your choice: "))
    match c:
        case 1:
            n=int(input("Enter number"))
            push(n)
        case 2:
            x=pop(l)
            print(x)
        case 3:
            x=top(l)
            print(x)
        case 4:
            isEmpty(l)
        case 5:
            size(l)
        case 6:
            display(l)
        case 7:
            break
        case _:
            print("Invalid choice")
