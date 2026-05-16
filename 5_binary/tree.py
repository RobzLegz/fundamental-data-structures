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

element = int(input("Enter element to insert: "))
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

while True:
    print("")
    print("Binary Tree Operations")
    print("1. Insert")
    print("2. Search")
    print("3. In-order Traversal")
    print("4. Display")
    print("5. Exit")
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
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(element)
                    break
                node = node.right

    elif choice == 2:
        element = int(input("Enter element to search: "))
        node = root
        while True:
            if element == node.data:
                print("Element found: ")
                print(node.return_printable())
                break
            elif element < node.data:
                node = node.left
            else:
                node = node.right

    elif choice == 3:
        print("In-order traversal: ")
        in_order_traversal(root)

    elif choice == 4:
        print_tree(root, 0)
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")

