while True:
    print("")
    print("Calculation Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square of Decimal Number")
    print("6. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 + num2

        print("Addition:", result)

    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 - num2

        print("Subtraction:", result)

    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 * num2

        print("Multiplication:", result)

    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2

            print("Division:", result)

    elif choice == 5:
        decimal_number = float(input("Enter decimal number: "))

        result = decimal_number ** 2

        print("Square:", result)

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")