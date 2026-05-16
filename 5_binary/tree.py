class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def return_printable(self):
        printable = {"data": self.data}

        if self.left is not None:
            printable["left"] = self.left.data

        if self.right is not None:
            printable["right"] = self.right.data

        return printable


element = int(input("Enter root element: "))
root = Node(element)


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print("    " * level + str(node.data))
        print_tree(node.left, level + 1)


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


def pre_order_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")


while True:
    print("")
    print("Binary Tree Operations")
    print("1. Insert")
    print("2. Search")
    print("3. In-order Traversal")
    print("4. Pre-order Traversal")
    print("5. Post-order Traversal")
    print("6. Display Tree")
    print("7. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to insert: "))

        node = root

        while True:
            if element == node.data:
                print("Element already exists")
                break

            elif element < node.data:
                if node.left is None:
                    node.left = Node(element)
                    print("Element inserted")
                    break

                node = node.left

            else:
                if node.right is None:
                    node.right = Node(element)
                    print("Element inserted")
                    break

                node = node.right

    elif choice == 2:
        element = int(input("Enter element to search: "))

        node = root
        found = False

        while node is not None:
            if element == node.data:
                print("Element found")
                print(node.return_printable())
                found = True
                break

            elif element < node.data:
                node = node.left

            else:
                node = node.right

        if not found:
            print("Element not found")

    elif choice == 3:
        print("In-order Traversal:")
        in_order_traversal(root)
        print()

    elif choice == 4:
        print("Pre-order Traversal:")
        pre_order_traversal(root)
        print()

    elif choice == 5:
        print("Post-order Traversal:")
        post_order_traversal(root)
        print()

    elif choice == 6:
        print("Binary Tree:")
        print_tree(root)

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
        