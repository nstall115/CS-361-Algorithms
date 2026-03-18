class Stack:
    # create stack
    def __init__(self):
        self.stack = []
    
    # add to stack
    def push(self, element):
        self.stack.append(element)

    # remove from stack
    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()
    
    # check top of stack
    def peek(self):
        if self.isEmpty():
            return -1         # error
        return self.stack[-1]
    
    # check if stack has elements
    def isEmpty(self):
        return len(self.stack) == 0
    
    # length or size of stack
    def size(self):
        return len(self.stack)
    

stack1 = Stack()
stack2 = Stack()

# add element to back of queue
def enqueue(element):
    stack1.push(element)

# remove element and return the front of queue
def dequeue():
    if(stack2.isEmpty()):
        # outbox is empty, refill the inbox
        # check if entire queue is empty
        if(stack1.isEmpty()):
            print("Queue is empty ")
            return
        # push outbox to inbox
        while not stack1.isEmpty():
            stack2.push(stack1.pop())
    # pop from the outbox  
    return stack2.pop()
    
# test
enqueue(1)
enqueue(2)
enqueue(3)
print(dequeue())
print(dequeue())
print(dequeue())