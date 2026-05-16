class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def return_printable(self):
        printable = {"data": self.data}
        if self.next is not None:
            printable["next"] = self.next.data

        return printable

linked_list = []

def print_linked_list():
    print([node.return_printable() for node in linked_list])

while True:
    print("")
    print("Linked List Operations")
    print("1. Insert at Head")
    print("2. Insert at Tail")
    print("3. Delete a Node")
    print("4. Display")
    print("5. Exit")
    print("")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to insert at head: "))
        node = Node(element)

        if len(linked_list) > 0:
            node.next = linked_list[0]

        linked_list.insert(0, node)
        print_linked_list()

    elif choice == 2:
        element = int(input("Enter element to insert at tail: "))
        node = Node(element)

        if len(linked_list) > 0:    
            prev_node = linked_list[-1]
            prev_node.next = node

        linked_list.append(node)
        print_linked_list()

    elif choice == 3:
        position = int(input("Enter position to delete: "))
        if position < 0 or position >= len(linked_list):
            print("Invalid position")
        else:
            if position > 0:
                prev_node = linked_list[position - 1]
                if position == len(linked_list) - 1:
                    prev_node.next = None
                else:
                    next_node = linked_list[position + 1]
                    prev_node.next = next_node

            linked_list.pop(position)
            print_linked_list()

    elif choice == 4:
        print_linked_list()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")