"""
The stack data structure is a sequential collection of element that follows the principle of Last In First out (LIFO)
The last element inserted into the stack is first element to be removed
A stack of plates. The last plate placed on top of the stack is also the first plate removed from the stack.
Stack is an abstract data type. It is defined by its behavior rather than being a mathematical model

The stack data structure supports two main operations
    1. Push, which adds an element to the collection
    2. Pop, which removes the most recently added element

Stack Usage
    - Browser history tacking
    - Undo operation when typing
    - Expression conversations
    - Call stack in JavaScript runtime

https://www.youtube.com/watch?v=a1fyufVlLmk&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=41
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)



# Creating a stack
stack = Stack()

# Checking if the stack is empty
print(stack.is_empty())  # Output: True

# Pushing elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Checking the size of the stack
print(stack.size())  # Output: 3

# Peeking at the top element
print(stack.peek())  # Output: 3

# Popping elements from the stack
print(stack.pop())    # Output: 3
print(stack.pop())    # Output: 2

# Checking the size after popping
print(stack.size())  # Output: 1

"""
Initialization (__init__): Time Complexity: O(1)
Explanation: The initialization involves creating an empty list, and creating an empty list is a constant-time operation.

is_empty: Time Complexity: O(1)
Explanation: Checking the length of a list and comparing it to zero is a constant-time operation.

push: Time Complexity: O(1)
Explanation: Appending an element to the end of a list is a constant-time operation on average.

pop: Time Complexity: O(1)
Explanation: Popping the last element from the end of a list is a constant-time operation.

peek: Time Complexity: O(1)
Explanation: Accessing the last element of a list (without removing it) is a constant-time operation.

size: Time Complexity: O(1)
Explanation: Returning the length of a list is a constant-time operation.
"""