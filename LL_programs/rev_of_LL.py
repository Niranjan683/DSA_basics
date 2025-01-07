class Node:
    def __init__(self,value=None, pointer = None):
        self.value = value
        self.pointer = pointer

class LinkedList:
    def __init__(self):
        self.head = None
    def add(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            cur = self.head
            while cur.pointer is not None:
                cur=cur.pointer
            cur.pointer = Node(value)
    def printt(self):
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur=cur.pointer 

    def rev_ll(self,prev=None):
        if prev:
            self.head = prev
        if self.head is None:
            return "Nothing to reverse" 
        if self.head.pointer is None:
            return self.head.value
        else:
            cur= self.head
            prev= None
            while cur is not None:
                t = cur.pointer
                cur.pointer = prev
                prev = cur
                cur = t 
        self.head = prev
ll=LinkedList()
ll.add(4)
ll.add(5)
ll.add(6)
print("Original LL")
ll.printt()

ll.rev_ll()
print("Reversed LL")
ll.printt()
