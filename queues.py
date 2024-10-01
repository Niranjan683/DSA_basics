class Queue:
    def __init__ (self):
        self.queues=[]
    def enqueue(self,n):
        self.queues.append(n)
    def dequeue(self):
        if self.isempty():
            return ("the queue is empty")
        return self.queues.pop(0)
    def peek(self):
        if self.isempty():
            return "The Queue Is Empty"
        return self.queues[0]
    def issize(self):
        return len(self.queues)


    def isempty(self):
        if len(self.queues)==0:
            return True
        return False
    
queue=Queue()

queue.enqueue('N')
queue.enqueue('I')
queue.enqueue('R')

print("Queue: ", queue.queues)

print("Dequeue: ", queue.dequeue())

print("Queue: ", queue.queues)

print("Peek: ", queue.peek())

print("isEmpty: ", queue.isempty())

print("Size: ", queue.issize())