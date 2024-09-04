from typing import Any, Optional

"""
Tutorial (02:23:00): https://youtu.be/8hly31xKli0?t=8580
"""


# Node class to represent each element in the linked list
class Node:
    def __init__(self, data: Any):
        # Initialize a Node with data and a pointer (next) set to None
        self.data: Any = data
        self.next: Node | Node = None

    def __repr__(self):
        # String representation of the Node, which shows its data value
        return "<Node Data: %s>" % self.data


# Singly linked list class, a data structure consisting of a chain of nodes
class SinglyLinkedList:
    """
    Singly linked list implementation
    """

    def __init__(self):
        # Initialize the linked list with head set to None (empty list)
        self.head: None | Node = None

    def is_empty(self) -> bool:
        # Returns True if the list is empty, otherwise False
        return self.head is None

    def size(self) -> int:
        # Returns the number of nodes in the list, complexity O(n)
        curr: Node = self.head  # Start with the head node
        count: int = 0  # Counter for the nodes
        while curr:
            # Traverse the list until reaching the end
            count += 1  # Increment the counter for each node
            curr = curr.next  # Move to the next node

        return count  # Return the total node count

    def insert(self, element: Any, index: int = 0) -> None:
        # Insert an element at a given index, defaulting to 0 (head insertion)
        if index == 0:
            # If inserting at index 0, add element at the head
            self.add(element)

        if index > 0:
            # If inserting at any other index
            new_node = Node(element)  # Create a new node with the element

            pos: int = index  # Position to insert at
            curr: Node | None = self.head  # Start at the head of the list
            while pos > 1:
                # Traverse to the node just before the insertion point
                curr = curr.next
                pos -= 1

            # Once at the insertion point, rearrange pointers
            prev_node = curr  # Node before insertion point
            next_node = curr.next  # Node after insertion point

            prev_node.next = new_node  # Link previous node to the new node
            new_node.next = next_node  # Link new node to the next node

    def remove(self, element: Any) -> Node | None:
        # Remove the first occurrence of the specified element in the list
        curr: Node | None = self.head  # Start from the head
        prev: Node | None = None  # Keep track of the previous node
        found: bool = False  # Flag to check if the element is found

        while curr and not found:
            if curr.data == element and curr == self.head:
                # If the element is found in the head, remove it by changing the head pointer
                found = True
                self.head = curr.next
            elif curr.data == element:
                # If the element is found in the middle or end, adjust the previous node's next pointer
                found = True
                prev.next = curr.next
            else:
                # Otherwise, move to the next node
                prev = curr
                curr = curr.next

        return curr  # Return the removed node (or None if not found)

    def remove_from_front(self) -> None | Node:
        if self.is_empty():
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    # Add a new element at the head of the list
    def add(self, element: Any) -> None:
        # O(1) complexity - Efficient for adding at the head
        new_node = Node(element)  # Create a new node with the element
        new_node.next = self.head  # Set the new node's next to the current head
        self.head = new_node  # Update the head to the new node

    def search(self, val: Any) -> Node | None:
        # Search for a node containing a specific value
        curr: Node | None = self.head  # Start from the head
        while curr:
            if curr.data == val:
                # If the current node contains the value, return it
                return curr
            else:
                # Otherwise, move to the next node
                curr = curr.next

        return None  # Return None if the value is not found

    def __repr__(self):
        # String representation of the linked list
        nodes = []
        curr: Node | None = self.head  # Start from the head

        while curr:
            if curr is self.head:
                # Mark the head node
                nodes.append("[Head: %s]" % curr.data)
            elif curr.next is None:
                # Mark the tail node
                nodes.append("[Tail: %s]" % curr.data)
            else:
                # Mark regular nodes
                nodes.append("[%s]" % curr.data)

            curr = curr.next  # Move to the next node

        return '-> '.join(nodes)  # Return a string representing the full list


# Creating an instance of the singly linked list
l = SinglyLinkedList()
l.add(10)  # Adding 10 at the head
l.add(20)  # Adding 20 at the head, becomes the new head
l.add(50)  # Adding 50 at the head
l.add(70)  # Adding 70 at the head
print(l)  # Print the list
print("Search: ", l.search(20))  # Search for the value 20 in the list
l.insert(150, 3)  # Insert 150 at index 3
print(l)  # Print the list after insertion
print("Remove: ", l.remove(50))  # Remove the node with value 50
print(l)  # Print the list after removal


# Node class for doubly linked list
class DoublyNode:
    def __init__(self, data: Any):
        self.data: Any = data  # Data of the node
        self.prev: Optional['DoublyNode'] = None  # Reference to the previous node
        self.next: Optional['DoublyNode'] = None  # Reference to the next node


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DoublyNode] = None  # Reference to the head of the list

    # Function to insert a node at the front
    def insert_front(self, data: Any) -> None:
        new_node: DoublyNode = DoublyNode(data)  # Create a new node
        new_node.next = self.head  # Point new node's next to the current head
        if self.head is not None:
            self.head.prev = new_node  # Set head's previous to new node
        self.head = new_node  # Update the head to be the new node

    # Function to insert a node after a given node
    def insert_after(self, prev_node: Optional[DoublyNode], data: Any) -> None:
        if prev_node is None:
            raise ValueError("Previous node cannot be None")
        new_node: DoublyNode = DoublyNode(data)  # Create a new node
        new_node.next = prev_node.next  # Point new node's next to prev_node's next
        prev_node.next = new_node  # Set prev_node's next to new node
        new_node.prev = prev_node  # Set new node's previous to prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node  # Update the next node's previous to new node

    # Function to append a node at the end
    def append(self, data: Any) -> None:
        new_node: DoublyNode = DoublyNode(data)  # Create a new node
        if self.head is None:  # If the list is empty, set new node as head
            self.head = new_node
            return
        last: DoublyNode = self.head  # Traverse to the last node
        while last.next:
            last = last.next
        last.next = new_node  # Set last node's next to new node
        new_node.prev = last  # Set new node's previous to last node

    # Function to delete a node from the list
    def delete_node(self, node: Optional[DoublyNode]) -> None:
        if self.head is None or node is None:
            return
        if node == self.head:  # If the node to be deleted is the head
            self.head = node.next  # Move head to the next node
        if node.next is not None:  # Update the next node's previous reference
            node.next.prev = node.prev
        if node.prev is not None:  # Update the previous node's next reference
            node.prev.next = node.next

    # Function to print the list from front to end
    def print_list(self) -> None:
        node: Optional[DoublyNode] = self.head
        while node:
            print(node.data, end=" <=> ")
            node = node.next
        print("None")


# Example usage:
dll = DoublyLinkedList()
dll.append(10)
dll.insert_front(5)
dll.append(15)
dll.insert_after(dll.head.next, 12)  # Inserting after the node with value 10

print("Doubly Linked List:")
dll.print_list()

dll.delete_node(dll.head.next)  # Delete the node with value 10
print("\nAfter deletion:")
dll.print_list()
