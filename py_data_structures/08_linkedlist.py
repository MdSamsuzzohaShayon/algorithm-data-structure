from typing import Any

"""
Tutorial (02:23:00): https://youtu.be/8hly31xKli0?t=8580
"""

# Node class to represent each element in the linked list
class Node:
    def __init__(self, data: Any):
        # Initialize a Node with data and a pointer (next) set to None
        self.data = data
        self.next = None

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
        self.head = None

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
