"""
In Python, you can implement a queue data structure using built-in lists. A queue follows the First In,
First Out (FIFO) principle, where the first element added is the first one to be removed.

Queue Usage
    Printers
    CPU task scheduling
    Callback queue in JavaScript runtime

https://www.youtube.com/watch?v=NuBWJ7kIlDg&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=43
"""

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")

    def size(self):
        return len(self.items)


# Creating a queue
queue = Queue()

# Checking if the queue is empty
print(queue.is_empty())  # Output: True

# Enqueueing elements into the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Checking the size of the queue
print(queue.size())  # Output: 3

# Peeking at the front element
print(queue.peek())  # Output: 1

# Dequeueing elements from the queue
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

# Checking the size after dequeueing
print(queue.size())  # Output: 1


"""
__init__: Time Complexity: O(1)
Explanation: The initialization of the queue involves creating an empty list, which is a constant time operation.

is_empty: Time Complexity: O(1)
Explanation: Checking whether the list is empty or not is a constant time operation.

enqueue: Time Complexity: O(1)
Explanation: Appending an element to the end of a list is a constant time operation.

dequeue: Time Complexity: O(n)
Explanation: Removing an element from the front of the list requires shifting all remaining elements to fill the gap. This results in a linear time operation because, in the worst case, you need to shift all elements.

peek: Time Complexity: O(1)
Explanation: Accessing the first element of the list is a constant time operation.

size: Time Complexity: O(1)
Explanation: Getting the length of a list is a constant time operation.
"""

