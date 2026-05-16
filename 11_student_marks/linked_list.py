class Node:
    def __init__(self, mark):
        self.mark = mark
        self.next = None

head = None

size = int(input("Enter number of students: "))

for i in range(size):
    mark = int(input("Enter mark of student " + str(i + 1) + ": "))

    new_node = Node(mark)

    if head is None:
        head = new_node
    else:
        current = head

        while current.next is not None:
            current = current.next

        current.next = new_node

while True:
    print("")
    print("Student Marks Linked List Operations")
    print("1. Display Marks")
    print("2. Calculate Average")
    print("3. Find Highest Mark")
    print("4. Find Lowest Mark")
    print("5. Search Student Mark")
    print("6. Add New Mark")
    print("7. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        current = head

        if current is None:
            print("No marks available")
        else:
            print("Student Marks:")
            while current is not None:
                print(current.mark, end=" ")
                current = current.next
            print()

    elif choice == 2:
        current = head
        total = 0
        count = 0

        while current is not None:
            total += current.mark
            count += 1
            current = current.next

        if count == 0:
            print("No marks available")
        else:
            average = total / count
            print("Average Mark:", average)

    elif choice == 3:
        if head is None:
            print("No marks available")
        else:
            highest = head.mark
            current = head.next

            while current is not None:
                if current.mark > highest:
                    highest = current.mark

                current = current.next

            print("Highest Mark:", highest)

    elif choice == 4:
        if head is None:
            print("No marks available")
        else:
            lowest = head.mark
            current = head.next

            while current is not None:
                if current.mark < lowest:
                    lowest = current.mark

                current = current.next

            print("Lowest Mark:", lowest)

    elif choice == 5:
        target = int(input("Enter mark to search: "))

        current = head
        position = 0
        found = False

        while current is not None:
            if current.mark == target:
                print("Mark found at position:", position)
                found = True
                break

            position += 1
            current = current.next

        if not found:
            print("Mark not found")

    elif choice == 6:
        mark = int(input("Enter new mark: "))

        new_node = Node(mark)

        if head is None:
            head = new_node
        else:
            current = head

            while current.next is not None:
                current = current.next

            current.next = new_node

        print("Mark added successfully")

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
        