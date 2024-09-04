from typing import Any

"""
Tutorial: https://youtu.be/-0ZIresFUZI?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
"""


# Node class to represent each element in the linked list
class Node:
    def __init__(self, data: Any):
        # Initialize a Node with data and a pointer (next) set to None
        self.data: Any = data
        self.next: Node | None = None

    def __repr__(self):
        # String representation of the Node, which shows its data value
        return "<Node Data: %s>" % self.data

class LinkedList:
    """
    Singly linked list implementation
    """

    def __init__(self):
        self.head: Node | None = None

    def is_empty(self) -> bool:
        # Returns True if the list is empty, otherwise False
        return self.head is None

    def size(self) -> int:
        # Returns the number of nodes in the list, complexity O(n)
        curr: Node = self.head
        count: int = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def insert(self, element: Any, index: int = 0) -> None:
        if index == 0:
            self.add(element)

        if index > 0:
            new_node = Node(element)

            pos: int = index
            curr: Node | None = self.head
            while pos > 1:
                curr = curr.next
                pos -= 1

            prev_node = curr
            next_node = curr.next

            prev_node.next = new_node
            new_node.next = next_node

    def remove_from_front(self) -> None | Node:
        if self.is_empty():
            return None
        val = self.head
        self.head = self.head.next
        return val

    def remove(self, element: Any) -> Node | None:
        curr: Node | None = self.head
        prev: Node | None = None
        found: bool = False

        while curr and not found:
            if curr.data == element and curr == self.head:
                found = True
                self.head = curr.next
            elif curr.data == element:
                found = True
                prev.next = curr.next
            else:
                prev = curr
                curr = curr.next

        return curr

    def add(self, element: Any) -> None:
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def search(self, val: Any) -> Node | None:
        curr: Node | None = self.head
        while curr:
            if curr.data == val:
                return curr
            else:
                curr = curr.next

        return None


    def __repr__(self):
        # String representation of the linked list
        nodes = []
        curr: Node | None = self.head

        while curr:
            if curr is self.head:
                nodes.append("[Head: %s]" % curr.data)
            elif curr.next is None:
                nodes.append("[Tail: %s]" % curr.data)
            else:
                nodes.append("[%s]" % curr.data)

            curr = curr.next  # Move to the next node

        return '-> '.join(nodes)


class LinkedListStack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, val: Any) -> None:
        self.list.add(val)

    def pop(self) -> Node | None:
        return self.list.remove_from_front()

    def peek(self) -> Any:
        return self.list.head

    def is_empty(self) -> bool:
        return self.list.is_empty()

    def get_size(self) -> int:
        return self.list.size()

    def print(self) -> LinkedList:
        return self.list


stack = LinkedListStack()
print("Empty? ", stack.is_empty())
stack.push(12)
stack.push(32)
stack.push(52)
stack.push(72)
print(stack.print())
stack.pop()
print(stack.print())
print("Peek ",stack.peek())
print("Size ",stack.get_size())
