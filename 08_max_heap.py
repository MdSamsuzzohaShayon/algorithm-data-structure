# https://www.youtube.com/watch?v=kQDxmjfkIKY&t=87s - 54:46
# MAXHEAP - COMPLETE BINARY TREE
# EVERY NODE <= ITS PARENT
# IT IS FAST
# INSERT IN O(log n)
# GET MAX IN O(1)
# REMOVE MAX IN O(log n)
# EASY TO IMPLEMENT
# USING A LIST
# A MAX HEAP ALWAYS BUBBLES THE HEIGHT VALUE TO THE TOP, SO IT CAN BE REMOVED INSTANTLY
# PUBLIC FUNCTIONS: PUSH, PEEK, POP
# PRIVATE FUNCTIONS: SWAP, __FLOATUP, BUBBLEDOWN, __STR

class MaxHeap:
    def __init__(self, items=[]):  # IF WE DON'T PASS THE ITEMS WE WILL GET EMPTY HEAP
        super().__init__()
        self.heap = [0]  # START OUR HEAP AT INDEX NUMBER 1 SO WE MADE FIRST ELEMENT 0 WHICH WILL NOT BE USED
        for item in items:
            self.heap.append(item)  # APPEND END OF THE HEAP
            self.__floatUp(len(self.heap) - 1)  # FLOATED UP TO THE PROPER POSITION

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):  # IT ONLY RETURNS TOP ITEM IN THE HEAP
        if (self.heap[1]):
            return self.heap[1]
        else:
            return False

    def pop(self):  # DEPEND OF HOW MANY ITEMS ON THE LIST
        if len(self.heap) > 2:  # IT THERE ARE MORE THAN 2 ITEMS IN THE HEAP
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:  # IF LIST HAS EXACT TWO ITEMS NA ONE OF THEM IS 0
            max = self.heap.pop()  # WE WILL POP OFF THAT ONE ITEM WITH INDEX NUMBER 1 AND WEILL RETURN IT
        else:
            max = False
        return max

    def __swap(self, i, j):  # SWAP TWO DIFFERENT ITEMS
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index): # RECEIVE AN INDEX OF THE ITEM THAT WE WANT TO FLOAT UP, PROBABLY THE VERY BOTTOM ITEM IN THE LIST INITIALLY
        parent = index // 2
        if index <= 1: # IF IT IS ALREADY IN THE TOP POSITION THEN THERE'S NO FLOATING UP TO DO
            return
        elif self.heap[index] > self.heap[parent]: # COMPARE IT TO ITS PARENT AND IF IT'S GREATER THAN ITS PARENT THEN THOSE TWO NEED TO SWAP PLACES
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index): #  TAKES AN ELEMENT THAT'S AT THE TOP OF THE LIST AND IT BUBBLES IT DOWN TO ITS PROPER POSITION
        left  = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)


m = MaxHeap([95, 3, 21])
m.push(10)
print(m) # [0, 95, 10, 21, 3]
print(m.pop()) # 95
print(m.peek()) # 21


