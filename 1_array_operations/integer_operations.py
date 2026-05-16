arr = []

while True:
    print("")
    print("Integer Array Operations")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element: "))
        position = int(input("Enter position: "))
        if position < 0 or position > len(arr):
            print("Invalid position")
        else:
            arr.insert(position, element)
            print("Element inserted successfully")

    elif choice == 2:
        position = int(input("Enter position to delete: "))
        if position < 0 or position >= len(arr):
            print("Invalid position")
        else:
            deleted = arr.pop(position)
            print(f"Deleted element: {deleted}")

    elif choice == 3:
        element = int(input("Enter element to search: "))
        if element in arr:
            print(f"Element found at position {arr.index(element)}")
        else:
            print("Element not found")

    elif choice == 4:
        print("Array:", arr)

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")