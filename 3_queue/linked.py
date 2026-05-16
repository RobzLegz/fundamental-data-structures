class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def return_printable(self):
        printable = {"data": self.data}
        if self.next is not None:
            printable["next"] = self.next.data
        if self.prev is not None:
            printable["prev"] = self.prev.data

        return printable

queue = []

def print_queue():
    print([node.return_printable() for node in queue])

while True:
    print("")
    print("Queue Operations")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Exit")
    print("")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = int(input("Enter element to enqueue: "))
        node = Node(element)

        if len(queue) > 0:
            prev_node = queue[-1]
            prev_node.next = node
            node.prev = prev_node
            queue.append(node)
        else:
            queue.append(node)

        print_queue()

    elif choice == 2:
        if len(queue) > 0:
            if len(queue) > 1:
                next_node = queue[1]
                next_node.prev = None
                queue.pop(0)
            else:
                queue.pop(0)
        else:
            print("Queue is empty")

        print_queue()

    elif choice == 3:
        if len(queue) > 0:
            print(queue[0].return_printable())
        else:
            print("Queue is empty")

    elif choice == 4:
        print("Exiting program...") 
        break

    else:
        print("Invalid choice")

