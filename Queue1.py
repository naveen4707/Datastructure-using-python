SIZE = 5  # Define maximum size of the queue
queue = [None] * SIZE
front = -1
rear = -1

def isEmpty():
    return front == -1 or front > rear

def isFull():
    return rear == SIZE - 1

def enqueue(value):
    global front, rear
    if isFull():
        print("Queue is FULL!!! Insertion is not possible!")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = value
        print(f"{value} inserted into the queue.")

def dequeue():
    global front, rear
    if isEmpty():
        print("Queue is EMPTY!!!")
    else:
        print(f"{queue[front]} is removed from the queue.")
        front += 1
        if front > rear:
            front = rear = -1  # Reset queue when empty

def size():
    if isEmpty():
        return 0
    return rear - front + 1

def show():
    if isEmpty():
        print("Queue is EMPTY!!!")
    else:
        print("Queue elements are:")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()

# ----------- Main Menu -------------
while True:
    print("\nQueue Operations Menu")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Size")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        val = input("Enter value to enqueue: ")
        enqueue(val)
    elif choice == '2':
        dequeue()
    elif choice == '3':
        show()
    elif choice == '4':
        print("Size of queue:", size())
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
