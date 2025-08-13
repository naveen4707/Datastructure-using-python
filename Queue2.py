
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{value} added to the queue.")

    
    def dequeue(self):
        if self.front is None:
            print("Queue is EMPTY!")
        else:
            removed = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(f"{removed} removed from the queue.")

    
    def display(self):
        if self.front is None:
            print("Queue is EMPTY!")
        else:
            temp = self.front
            print("Queue:", end=" ")
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("NULL")


q = Queue()

while True:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        val = input("Enter value to enqueue: ")
        q.enqueue(val)
    elif ch == '2':
        q.dequeue()
    elif ch == '3':
        q.display()
    elif ch == '4':
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")
