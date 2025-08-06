

stack = []
Max = 5
top = -1

def push(book):
    global top
    if top == Max - 1:
        print("Stack is full. Cannot add more books.")
    else:
        top += 1
        stack.append(book)
        print("Book added:", book)

def pop():
    global top
    if top == -1:
        print("Stack is empty. Cannot remove books.")
    else:
        removed_book = stack.pop()
        print("Book removed:", removed_book)
        top -= 1

def peek():
    if top == -1:
        print("Stack is empty.")
    else:
        print("Top book is:", stack[top])
while True:
    print("\n1. Push book")
    print("2. Pop book")
    print("3. Peek book")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        title = input("Enter the book name: ")
        push(title)
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
