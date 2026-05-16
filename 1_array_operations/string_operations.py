string_var = ""

while True:
    print("")
    print("String Operations")
    print("1. Insert Character")
    print("2. Delete Character")
    print("3. Search Character")
    print("4. Display String")
    print("5. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ch = input("Enter character: ")
        while len(ch) != 1:
            print("Please enter only one character")
            ch = input("Enter character: ")

        position = int(input("Enter position: "))
        if position < 0 or position > len(string_var):
            print("Invalid position")
        else:
            string_var = string_var[:position] + ch + string_var[position:]
            print("Character inserted successfully")

    elif choice == 2:
        position = int(input("Enter position to delete: "))
        if position < 0 or position >= len(string_var):
            print("Invalid position")
        else:
            deleted = string_var[position]
            string_var = string_var[:position] + string_var[position + 1:]
            print(f"Deleted character: {deleted}")

    elif choice == 3:
        ch = input("Enter character to search: ")
        if ch in string_var:
            print(f"Character found at position {string_var.index(ch)}")
        else:
            print("Character not found")

    elif choice == 4:
        if string_var == "":
            print("String is empty")
        else:
            print("String:", string_var)

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")