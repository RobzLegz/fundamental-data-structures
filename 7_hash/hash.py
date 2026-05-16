TABLE_SIZE = 10

table = [[] for _ in range(TABLE_SIZE)]

def hash_function(key):
    return hash(key) % TABLE_SIZE

def insert(key, value):
    index = hash_function(key)

    for pair in table[index]:
        if pair[0] == key:
            pair[1] = value
            return

    table[index].append([key, value])


def get(key):
    index = hash_function(key)

    for pair in table[index]:
        if pair[0] == key:
            return pair[1]

    return None


def display():
    print("")
    print("Hash Table:")
    
    for i, bucket in enumerate(table):
        print(i, ":", bucket)


while True:
    print("")
    print("1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")

        insert(key, value)

        print("Data inserted.")

    elif choice == "2":
        key = input("Enter key to search: ")

        result = get(key)

        if result is not None:
            print(f"Value: {result}")
        else:
            print("Key not found.")

    elif choice == "3":
        display()

    elif choice == "4":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")
        