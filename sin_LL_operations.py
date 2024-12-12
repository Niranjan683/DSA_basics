"""   BASIC OPERATIONS LIKE ADD, INSERT, DELETE,   """



class Node:
    def __init__(self,value=None,pointer=None):
        self.value = value
        self.pointer = pointer
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def add(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            cur=self.head
            while cur.pointer is not None:
                cur=cur.pointer
            cur.pointer=Node(value)
            
    def print(self):
        if self.head is None:
            print('empty')
        else:
            cur = self.head
            while cur is not None:
                print(cur.value)
                cur =cur.pointer
            
    def delete(self,value):
        prev = self.head
        cur = prev.pointer
        while prev.pointer is not None:
            if cur.value ==value:
                prev.pointer=cur.pointer
                break
            prev=prev.pointer
                
                
    def insert(self,aftr,value):
        cur = self.head
        self.newnode = Node(value) 
        while cur is not None:
            if cur.value == aftr:
                self.newnode.pointer = cur.pointer
                cur.pointer = self.newnode
            cur=cur.pointer
            
    def update(self,cur_val,new_val):
        cur =self.head
        while cur is not None:
            if cur.value == cur_val:
                cur.value = new_val
            cur = cur.pointer
                
                
            
ll=LinkedList()
print("adding element in LL")
ll.add(5)
ll.add(6)
ll.add(7)
ll.add(8)
ll.print()
print("deletion")
ll.delete(6)
ll.print()
print("Inserting")
ll.insert(5,6)
ll.print()
print("update value")
ll.update(8,9)
ll.print()            