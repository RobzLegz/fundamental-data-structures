numbers = []

size = int(input("Enter number of elements: "))

for i in range(size):
    element = int(input("Enter element: "))
    numbers.append(element)

while True:
    print("")
    print("Linear Search Operations")
    print("1. Display List")
    print("2. Search Element")
    print("3. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current List:")
        print(numbers)

    elif choice == 2:
        target = int(input("Enter element to search: "))

        found = False

        for i in range(len(numbers)):
            if numbers[i] == target:
                print("Element found at index:", i)
                found = True
                break

        if not found:
            print("Element not found")

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
        