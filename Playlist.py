EX.2
class Node:  
    def __init__(self, song):
        self.song, self.next = song, None
class Playlist:  
    def __init__(self):
        self.head = None
    def add(self, song):  
        n = Node(song)  
        if not self.head:
            self.head = n  
        else:  
            t = self.head  
            while t.next:
                t = t.next  
            t.next = n
    def show(self):  
        t = self.head  
        print("Empty" if not t else "", end="")  
        while t:
            print("->", t.song, end=" "); t = t.next  
        print()
    def insert(self, song, pos):  
        n = Node(song)  
        if pos == 0:
            n.next, self.head = self.head, n; return  
        t = self.head  
        for _ in range(pos-1):
            t = t.next if t else None  
        if not t:
            return  
        n.next, t.next = t.next, n
    def delete(self, song):  
        t, p = self.head, None  
        while t and t.song != song:
            p, t = t, t.next  
        if not t:
            return  
        if not p:
            self.head = t.next  
        else:
            p.next = t.next
p = Playlist()  
while True:  
    c = input("1-Add 2-Show 3-Insert 4-Del 5-Exit: ")  
    if c == '1':
        p.add(input("Song: "))  
    elif c == '2':
        p.show()  
    elif c == '3':
        p.insert(input("Song: "), int(input("Pos: ")))  
    elif c == '4':
        p.delete(input("Song: "))  
    elif c == '5': bresk
