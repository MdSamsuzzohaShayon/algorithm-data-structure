"""
https://www.youtube.com/watch?v=ba15sgOiAOg&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=44
"""

class Queue:
    def __init__(self):
        self.items = {}
        self.rear = 0
        self.front = 0

    def enqueue(self, element):
        self.items[self.rear] = element
        self.rear += 1

    def dequeue(self):
        item = self.items[self.front]
        del self.items[self.front]
        self.front += 1
        return item

    def is_empty(self):
        return self.rear - self.front == 0

    def peek(self):
        return self.items[self.front]

    def size(self):
        return self.rear - self.front

    def print_queue(self):
        print(self.items)


# Example usage
queue = Queue()
print(queue.is_empty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(40)
queue.enqueue(90)
print(queue.size())
queue.print_queue()
print(queue.dequeue())
print(queue.peek())


"""
enqueue(element): Time Complexity: O(1)
Explanation: Appending an element to a dictionary at a specific key (self.rear) is a constant time operation.

dequeue(): Time Complexity: O(1)
Explanation: Retrieving and deleting an element from the dictionary, and incrementing self.front, are constant time operations.

is_empty(): Time Complexity: O(1)
Explanation: The operation involves checking if the difference self.rear - self.front is equal to 0, which is a constant time operation.

peek(): Time Complexity: O(1)
Explanation: Accessing the element at the front of the queue in the dictionary is a constant time operation.

size(): Time Complexity: O(1)
Explanation: Calculating the size of the queue involves subtracting self.front from self.rear, which is a constant time operation.

print_queue(): Time Complexity: O(n)
Explanation: Printing all elements in the queue involves iterating through the dictionary. In the worst case, this is a linear time operation, where 'n' is the number of elements in the queue.

"""