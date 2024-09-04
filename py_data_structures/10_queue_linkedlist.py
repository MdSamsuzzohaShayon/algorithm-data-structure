from typing import Any

"""
Tutorial: https://youtu.be/15q-fLZqo_0?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
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
        self._head: Node | None = None

    def is_empty(self) -> bool:
        # Returns True if the list is empty, otherwise False
        return self._head is None

    def size(self) -> int:
        # Returns the number of nodes in the list, complexity O(n)
        curr: Node = self._head
        count: int = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def insert(self, element: Any, index: int = 0) -> None:
        if index == 0:
            self.prepend(element)

        if index > 0:
            new_node = Node(element)

            pos: int = index
            curr: Node | None = self._head
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
        val = self._head
        self._head = self._head.next
        return val

    def remove(self, element: Any) -> Node | None:
        curr: Node | None = self._head
        prev: Node | None = None
        found: bool = False

        while curr and not found:
            if curr.data == element and curr == self._head:
                found = True
                self._head = curr.next
            elif curr.data == element:
                found = True
                prev.next = curr.next
            else:
                prev = curr
                curr = curr.next

        return curr

    # Prepend
    def prepend(self, element: Any) -> None:
        new_node = Node(element)
        new_node.next = self._head
        self._head = new_node

    def append(self, element: Any) -> None:
        # add element at the end of the list
        new_node  = Node(element)
        if self.is_empty():
            self._head = new_node
        else:
            curr = self._head
            while curr.next:
                curr = curr.next
                # Setting the last node
            curr.next = new_node

    def search(self, val: Any) -> Node | None:
        curr: Node | None = self._head
        while curr:
            if curr.data == val:
                return curr
            else:
                curr = curr.next

        return None


    def __repr__(self):
        # String representation of the linked list
        nodes = []
        curr: Node | None = self._head

        while curr:
            if curr is self._head:
                nodes.append("[Head: %s]" % curr.data)
            elif curr.next is None:
                nodes.append("[Tail: %s]" % curr.data)
            else:
                nodes.append("[%s]" % curr.data)

            curr = curr.next  # Move to the next node

        return '-> '.join(nodes)


class LinkedListQueue:
    def __init__(self):
        self._list: LinkedList = LinkedList()

    def enqueue(self, val: Any) -> None:
        self._list.append(val)

    def dequeue(self) -> Node | None:
        return self._list.remove_from_front()

    def peek(self) -> Node | None:
        return self._list._head

    def is_empty(self) -> bool:
        return self._list.is_empty()

    def get_size(self) -> int:
        return self._list.size()

    def print(self) -> LinkedList:
        return self._list


queue = LinkedListQueue()
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(70)
queue.enqueue(10)
print(queue.print())
queue.dequeue()
print(queue.print())
print(queue.peek())
