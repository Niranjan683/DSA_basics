class Node:
    def __init__(self,data):
        self.data=data
        self.child=[]
class Tree:
    def __init__(self):
        self.root=None
    def add(self,data,parentdata=None):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        parentnode =self.findparentnode(parentdata,self.root)
        if not parentnode:
            print(' parent node not found')
            return
        parentnode.child.append(node)

    def findparentnode(self,parentdata,node) :
        
        if node.data == parentdata:
            return node
        for child in node.child:
            nodefound=self.findparentnode(parentdata,child)
            if nodefound is not None:
                return nodefound
        return None
    
    
    def display(self,node):
        print(node.data)
        for ch in node.child:
            self.display(ch)

            
             


tree=Tree()
tree.add(1)
tree.add(2,1) 
tree.add(3,1) 
tree.add(4,2)                
tree.add(5,2) 
tree.add(6,3) 
tree.display(tree.root)