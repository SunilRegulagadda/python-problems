queue=list(map(int,input("enter the elements of queue").split()))
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Rare")
    print("5. Exit")
    print()
    c=int(input("Enter your choice"))
    match c:
        case 1:
            a=int(input("enter element to append"))
            queue.append(a)
        case 2:
            if(len(queue)==0):
                print("Queue is empty")
            else:
                dq=queue.pop()
                print("popped element is",dq)
                print(queue)
        case 3:
            if len(queue) == 0:
                print("queue is empty")
            else:
                print("front is",queue[0])
        case 4:
            if len(queue) == 0:
                print("queue is empty")
            else:
                print("rare is",queue[-1])
        case 5:
            break
        case _:
            print("Invalid choice")