queue = []

while True:
    print("")
    print("Queue Operations")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Exit")
    print("")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = int(input("Enter element to enqueue: "))
        queue.append(element)
        print(queue)

    elif choice == 2:
        if len(queue) > 0:
            el = queue.pop(0)
            print(f"Dequeued element: {el}")
            print(queue)
        else:
            print("Queue is empty")

    elif choice == 3:
        if len(queue) > 0:
            print(queue[0])
        else:
            print("Queue is empty")
            
    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")