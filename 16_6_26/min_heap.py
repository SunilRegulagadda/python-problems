import heapq
print("Enter the elements of the heap (space separated): ")
l=list(map(int,input().split()))
h=heapq.heapify(l)
print(l)
while True:
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Display the minimum element")
    print("4. Exit")
    ch=int(input("Enter your choice: "))
    match ch:
        case 1:
            x=int(input("Enter the element to be inserted: "))
            heapq.heappush(l, x)
            print(l)
        case 2:
            x=int(input("Enter the element to be deleted: "))
            l.remove(x)
            heapq.heapify(l)
            print(l)
        case 3:
            print("The minimum element is:", heapq.heappop(l))
        case 4:
            break
        case _:
            print("Invalid choice! Please try again.")