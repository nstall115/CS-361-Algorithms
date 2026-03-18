class Stack:
    # create stack
    def __init__(self):
        self.stack = []
    
    # add to stack
    def push(self, element):
        self.stack.append(element)

    # push off of stack
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

def solveTowers(n, tower1, tower2, tower3):
    # tower1 is the starting source
    # tower2 is the aux tower
    # tower3 is the target tower
    if n == 0:
        return

    solveTowers(n - 1, tower1, tower3, tower2)
    tower3.push(tower1.pop())
    #print(f"Moving disk {n} A:{tower1.stack} B:{tower2.stack} C:{tower3.stack}")
    print(f"Move disk {n} from Tower A to Tower C")
    solveTowers(n - 1, tower2, tower1, tower3)

n = 5

tower1 = Stack()
tower2 = Stack()
tower3 = Stack()

# creates tower1's stack based off value n
for i in range(n, 0, -1):
    tower1.push(i)

print("Starting Tower (A): ", tower1.stack)
solveTowers(n, tower1, tower2, tower3)
print("Ending Tower (C): ", tower3.stack)