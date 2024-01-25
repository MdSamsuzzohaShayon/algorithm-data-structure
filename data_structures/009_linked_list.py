"""
YouTube Tutorial-1: https://www.youtube.com/watch?v=3OsxH-huRc4&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=47
YouTube Tutorial-2: https://www.youtube.com/watch?v=Tggvw4QlA9U&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=48
YouTube Tutorial-3: https://www.youtube.com/watch?v=NAPQ0ua02CA&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=49
Linked lists are data structures that consist of nodes, where each node contains a data element and a reference (link) to the next node in the sequence

Drawbacks:
    Random access of elements is not feasible
    Accessing an element has linear time complexity

3 Main operations:
    Insert - To add an element at the beginning, and or at the given index
    Delete - To remove an element from the given index or value
    Search - To find an element at given value

Usages:
    All application of both stacks and queues are application of linked list

Example:
    Image viewer
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def prepend(self, value): # Adding an element at the beginning of the list
        node = Node(value=value)
        if not self.is_empty():
            node.next = self.head
        self.head = node
        self.size += 1



ll = LinkedList()
print(f"List is empty? {ll.is_empty()}")
print(f"List size {ll.get_size()}")

ll.prepend(10)
ll.prepend(20)
ll.prepend(30)