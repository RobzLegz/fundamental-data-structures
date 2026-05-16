stack = []

while True:
    print("")
    print("Stack Operations")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to push: "))
        stack.append(element)
        print(stack)

    elif choice == 2:
        if len(stack) > 0:
            el = stack.pop()
            print(f"Popped element: {el}")
        else:
            print("Stack is empty")

    elif choice == 3:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print("Stack is empty")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")