numbers = []

size = int(input("Enter number of elements: "))

for i in range(size):
    element = int(input("Enter element: "))
    numbers.append(element)

while True:
    print("")
    print("Bubble Sort Operations")
    print("1. Display List")
    print("2. Sort List")
    print("3. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current List:")
        print(numbers)

    elif choice == 2:
        n = len(numbers)

        for i in range(n):
            for j in range(0, n - i - 1):

                if numbers[j] > numbers[j + 1]:
                    temp = numbers[j]
                    numbers[j] = numbers[j + 1]
                    numbers[j + 1] = temp

        print("List sorted successfully")
        print("Sorted List:")
        print(numbers)

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")