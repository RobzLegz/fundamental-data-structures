class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    def level_order(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)
            print(current.value, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

    def search(self, value):
        if self.root is None:
            return False

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.value == value:
                return True

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return False

    def count_nodes(self, node):
        if node is None:
            return 0

        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def display(self):
        if self.root is None:
            print("Tree is empty")
        else:
            print("Tree elements in level order:")
            self.level_order()
            print()

tree = BinaryTree()

while True:
    print("")
    print("Binary Tree Operations")
    print("1. Insert")
    print("2. Preorder Traversal")
    print("3. Inorder Traversal")
    print("4. Postorder Traversal")
    print("5. Level Order Traversal")
    print("6. Search")
    print("7. Count Nodes")
    print("8. Height of Tree")
    print("9. Display Tree")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        tree.insert(value)
        print("Inserted successfully")

    elif choice == 2:
        print("Preorder Traversal:")
        tree.preorder(tree.root)
        print()

    elif choice == 3:
        print("Inorder Traversal:")
        tree.inorder(tree.root)
        print()

    elif choice == 4:
        print("Postorder Traversal:")
        tree.postorder(tree.root)
        print()

    elif choice == 5:
        print("Level Order Traversal:")
        tree.level_order()
        print()

    elif choice == 6:
        value = int(input("Enter value to search: "))
        if tree.search(value):
            print("Value found")
        else:
            print("Value not found")

    elif choice == 7:
        print("Total nodes:", tree.count_nodes(tree.root))

    elif choice == 8:
        print("Height of tree:", tree.height(tree.root))

    elif choice == 9:
        tree.display()

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")