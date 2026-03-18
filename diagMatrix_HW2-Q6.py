# Question 6. A matrix diagonal is a diagonal line of cells starting from some cell in
# either the topmost row or leftmost column and going in the bottom-right direction until
# reaching the matrix's end. Write a solution for a given m × n matrix of integers, sort each
# matrix diagonal in ascending order and return the resulting matrix.
# Following is an example:
# Input:   Output:
# 3 3 1 1  1 1 1 1
# 2 2 1 2  1 2 2 2
# 1 1 1 2  1 2 3 3

class Heap:
    # create heap
    def __init__(self):
        self.heap = []
    
    # add element
    def push(self, element):
        self.heap.append(element)
        self.bubbleUp(len(self.heap) - 1)

    # remove element
    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # move last element to root
        self.bubbleDown(0)
        return root
    
    # check smallest
    def peek(self):
        return self.heap[0]
    
    # checks if there are elemtents
    def isEmpty(self):
        return len(self.heap) == 0
    
    # checks length or size
    def size(self):
        return len(self.heap)

    def top  (self, i): return (i - 1) // 2 # top of the index node's parent
    def lSide(self, i): return 2 * i + 1    # index node of left child
    def rSide(self, i): return 2 * i + 2    # index node of right child

    # bubble sort
    def bubbleUp(self, i):
        # loops O(log n) times
        while i > 0:
            parent = self.top(i)
            # if current node is smaller violates the heap
            if  self.heap[i]< self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i] # swap heap
                i = parent
            else:
                break # condition ok break

    def bubbleDown(self, i):
        size = len(self.heap)
        # loops O(log n) times
        while True:
            smallest = i
            left  = self.lSide(i)
            right = self.rSide(i)
            # checks if right is smallest
            if left  < size and self.heap[left]  < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            # if smaller replace
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            # exit condition
            else:
                break

inputMatrix = [[3,3,1,1],
               [2,2,1,2],
               [1,1,1,2]]

print("Unsorted Matrix: ", inputMatrix)

def solve(inputMatrix):
    rows = len(inputMatrix)    # m
    cols = len(inputMatrix[0]) # n

    sortDiagonal = {}

    # pass 1
    for i in range(rows):
        for j in range(cols):
            key = j - i                               # codiagonal cells
            if key not in sortDiagonal:
                sortDiagonal[key] = Heap()
            sortDiagonal[key].push(inputMatrix[i][j]) # create heap

    # pass 2
    for i in range(rows):
        for j in range(cols):
            key = j - i
            inputMatrix[i][j] = sortDiagonal[key].pop()

    return inputMatrix

print("Sorted Matrix: ", solve(inputMatrix))