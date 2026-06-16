import heapq
print("Enter the elements of the heap (space separated): ")
l=list(map(int,input().split()))
h=[-x for x in l]
heapq.heapify(h)
print("Max heap:", [-x for x in h])
while True:
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Display the maximum element")
    print("4. Exit")
    ch=int(input("Enter your choice: "))
    match ch:
        case 1:
            x=int(input("Enter the element to be inserted: "))
            heapq.heappush(h, -x)
            print("Max heap:", [-x for x in h])
        case 2:
            x=int(input("Enter the element to be deleted: "))
            h.remove(-x)
            heapq.heapify(h)
            print("Max heap:", [-x for x in h])
        case 3:
            print("The maximum element is:", -heapq.heappop(h))
        case 4:
            break
        case _:
            print("Invalid choice! Please try again.")