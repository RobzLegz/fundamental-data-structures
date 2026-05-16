marks = []

size = int(input("Enter number of students: "))

for i in range(size):
    mark = int(input("Enter mark of student " + str(i + 1) + ": "))
    marks.append(mark)

while True:
    print("")
    print("Student Marks Operations")
    print("1. Display Marks")
    print("2. Calculate Average")
    print("3. Find Highest Mark")
    print("4. Find Lowest Mark")
    print("5. Search Student Mark")
    print("6. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Student Marks:")
        print(marks)

    elif choice == 2:
        total = 0

        for mark in marks:
            total += mark

        average = total / len(marks)

        print("Average Mark:", average)

    elif choice == 3:
        highest = marks[0]

        for mark in marks:
            if mark > highest:
                highest = mark

        print("Highest Mark:", highest)

    elif choice == 4:
        lowest = marks[0]

        for mark in marks:
            if mark < lowest:
                lowest = mark

        print("Lowest Mark:", lowest)

    elif choice == 5:
        target = int(input("Enter mark to search: "))

        if target in marks:
            print("Mark found at position:", marks.index(target))
        else:
            print("Mark not found")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")