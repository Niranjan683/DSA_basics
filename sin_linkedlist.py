class Node:
    def __init__(self,data):
        
        self.head = data 
        self.pointer=None
class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data):
        self.newnode=Node(data)
        if self.head is None:
            self.head=self.newnode
        else:
            cur=self.head
            while cur.pointer is not None:
                cur=cur.pointer
            cur.pointer= self.newnode
    
    def print(self):
        
        if self.head is None:
            print('empty')  
        else:
            cur=self.head
            while cur is not None:
                print(cur.head)
                cur=cur.pointer

LinkedList=LinkedList()
LinkedList.add(1)
LinkedList.add(26)
'''LinkedList.add(3)
LinkedList.add(4)'''
LinkedList.print()