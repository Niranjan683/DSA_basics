class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,n):
        self.stack.append(n)
    def pop(self):
        if self.isempty():
            return "The Stack Is Empty"
        return self.stack.pop()
    def peek(self):
        if self.isempty():
            return "The Stack Is Empty"
        return self.stack[-1]
    def isempty(self):
        if len(self.stack)==0:
            return True
        return False
    def issize(self):
        return len(self.stack)


stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print('stack : ', stack.stack)
print('pop :',stack.pop()) 
print('stack : ', stack.stack) 
print('is empty:',stack.isempty()) 
print('Top element :',stack.peek())           
print('The size is :',stack.issize()) 