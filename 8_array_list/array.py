class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity

    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data

    def append(self, value):
        if self.size == self.capacity:
            self._resize()

        self.data[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if self.size == self.capacity:
            self._resize()

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    def remove(self, value):
        index = self.index_of(value)

        if index == -1:
            print("Value not found")
            return

        self.pop(index)

    def pop(self, index=-1):
        if self.size == 0:
            print("List is empty")
            return None

        if index < 0:
            index += self.size

        if index < 0 or index >= self.size:
            print("Index out of range")
            return None

        removed = self.data[index]

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1

        return removed

    def get(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return None

        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return

        self.data[index] = value

    def index_of(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def display(self):
        print([self.data[i] for i in range(self.size)])

size = int(input("Enter number of initial elements: "))

arr = ArrayList(size)

print("Enter elements:")
for _ in range(size):
    value = int(input())
    arr.append(value)

while True:
    print("")
    print("Array List Operations")
    print("1. Append")
    print("2. Insert")
    print("3. Remove by value")
    print("4. Pop by index")
    print("5. Get element")
    print("6. Set element")
    print("7. Display list")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value to append: "))
        arr.append(value)

    elif choice == 2:
        index = int(input("Enter index: "))
        value = int(input("Enter value: "))
        arr.insert(index, value)

    elif choice == 3:
        value = int(input("Enter value to remove: "))
        arr.remove(value)

    elif choice == 4:
        index = int(input("Enter index to pop: "))
        removed = arr.pop(index)
        if removed is not None:
            print("Removed:", removed)

    elif choice == 5:
        index = int(input("Enter index: "))
        result = arr.get(index)
        if result is not None:
            print("Element:", result)

    elif choice == 6:
        index = int(input("Enter index: "))
        value = int(input("Enter new value: "))
        arr.set(index, value)

    elif choice == 7:
        print("Current List:")
        arr.display()

    elif choice == 8:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
