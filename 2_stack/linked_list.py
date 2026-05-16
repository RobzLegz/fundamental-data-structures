class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_printable(self):
        printable = {"data": self.data}
        if self.next is not None:
            printable["next"] = self.next.data
        return printable

stack = []

def print_stack():
    print([node.get_printable() for node in stack])

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
        node = Node(element)

        if len(stack) > 0:
            prev_node = stack[-1]
            prev_node.next = node

            stack.append(node)
        else:
            stack.append(node)

        print_stack()

    elif choice == 2:
        if len(stack) > 0:
            prev_node = stack[-1]
            prev_node.next = None

            stack.pop()
        else:
            print("Stack is empty")

        print_stack()

    elif choice == 3:
        if len(stack) > 0:
            print(stack[-1].get_printable())
        else:
            print("Stack is empty")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")