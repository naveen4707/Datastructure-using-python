class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    def push(self,title):
        new_node=node(title)
        new_node.next=self.top
        self.top=new_node
        print("pushed:",title)
    def pop(self):
        if self.top is None:
            print("stack is empty")
        else:
            print("popped:",self.top.data)
            self.top=self.top.next
    def display(self):
        if self.top is None:
            print("stack is empty")
        else:
            tmp=self.top
            while tmp:
                print(tmp.data,end="->")
                tmp=tmp.next
            print("Null")

stack=stack()
stack.push("book A")
stack.push("book B")
stack.display()
stack.pop()
stack.display()
