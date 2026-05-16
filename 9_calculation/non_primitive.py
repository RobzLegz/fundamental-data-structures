numbers = []

while True:
    print("")
    print("List Operations")
    print("1. Add Element")
    print("2. Remove Element")
    print("3. Search Element")
    print("4. Display List")
    print("5. Update Element")
    print("6. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to add: "))

        numbers.append(element)

        print("Element added successfully")

    elif choice == 2:
        element = int(input("Enter element to remove: "))

        if element in numbers:
            numbers.remove(element)

            print("Element removed successfully")
        else:
            print("Element not found")

    elif choice == 3:
        element = int(input("Enter element to search: "))

        if element in numbers:
            print("Element found at index:", numbers.index(element))
        else:
            print("Element not found")

    elif choice == 4:
        print("Current List:")

        if len(numbers) == 0:
            print("List is empty")
        else:
            print(numbers)

    elif choice == 5:
        index = int(input("Enter index to update: "))

        if index >= 0 and index < len(numbers):
            new_value = int(input("Enter new value: "))

            numbers[index] = new_value

            print("Element updated successfully")
        else:
            print("Invalid index")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")