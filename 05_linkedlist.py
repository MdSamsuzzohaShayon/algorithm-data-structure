# 02:25:00 - singly linked list

class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None  # hold on to the data that we are storing
    next_node = None  # to point to the next node in the list

    def __init__(self, data):
        self.data = data

        # The string representations of the numeric classes, computed by __repr__() and __str__()
        # https://docs.python.org/3/reference/datamodel.html#object.__repr__

    def __repr__(self):
        return "<Node data: %s>" % self.data


# Linkedlist class is going to define a head
# Strength of linkedlist comes in insert and delete operation
class LinkedList:
    """
    Singly linkedlist 
    if the list is empty we would need to query these instance variables head and so on every time.
    """

    def __init__(self):
        self.head = None

    """
    Ideally we would like to not espose the inner workings of our data structure t code that uses it
    Instead let's make this operation more explicit by defining a method (is_empty)
    """

    def is_empty(self):
        return self.head == None

    """
    convineant method to calculate the size of the list
    do not provide any additional function  that data structure can not handle right now
    We could calculate the size of our linkedlist by traversing it everytime using a loop until we hit a tail node
    We need to visit every node to determine the size of the node, therefore, our algorithm runs in linear time
    Returns the number of nodes in the list takes 0(n) time 
    """

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds new node containing data at head of the list takes 0(1) time
        because the insert operation is simply a reassignment of the head and next node properties this is a constant time operation
        """
        new_node = Node(data)
        # node's next property at whatever node is currently at head
        new_node.next_node = self.head
        self.head = new_node
        # Insert operation is simply reassignment of the head and next node properties this is a constant time operation

    # Unlike array where at the time of insertion all element after the particular index need to be shifted
    # With linkedlist we just need to change the references to the next on a few nodes
    # to insert a node at specific index we need to modify a node after the index node and modify a node before the index node in this way insert is a constant time operation
    # we do not need to shift all the element of the list
    def insert(self, data, index):
        """
        :param data: insert take data at index position
        :param index: data at index position
        :return:
        insertion takes constant time operation O(1) time but find the node at the insertion point takes linear O(n) time!
        take overall linear O(n) time
        """
        if index == 0:
            self.add(data)
        # traverse the list to find the current node at that index
        if index > 0:
            new_node  = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = new_node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    # new to modify next node references
    # the node before the match needs to point to the node after the match
    def remove(self, key):
        """
        :param key: Remove node containing data that matches the key
        :return: returns the node or none if the key does not exist
        This take linear O(n) time
        """
        current = self.head
        previous = None
        found = False

        # Use loop to keep traversing the linkedlist as long as found is false
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current


    # return the node if it is found otherwise return None
    def search (self, key):
        """
        :param key: Search the first node containing data that matches the key
        :return: the node or None if not found
        In the worst case scenario we will need to check every single node in the list before we find the key or fail
        As a result this operation runs in linear time os it takes O(n)
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None

    def __repr__(self):
        """
        :return: a string representation of the list
        :param: take 0(n) time
        """
        nodes = []  # python list of string
        current = self.head  # pointer to the head node

        # Until we reach the tail we are going to implement some logic
        while current:
            # if current is same as head that means this is the first node or head node
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
                # if we get the tail node
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
                # not head or tail
            else:
                nodes.append("[%s]" % current.data)
            # With every iteration of the loop we move current forward
            current = current.next_node
        return '-> '.join(nodes)


# Enter interactive mode afterwards. This can be done by passing -i before the script.
# python3 -i 05_linkedlist.py
"""
>>> n1 = Node(10)
>>> n1
<Node data: 10>
>>> n2 = Node(20)
>>> n1.next_node = n2
>>> n2
<Node data: 20>
>>> n1
<Node data: 10>
>>> n1.next_node
<Node data: 20>
>>> 
"""

# Check size and add function
"""
>>> l = LinkedList()
>>> l.add(2)
>>> l.add(5)
>>> l.add(6)
>>> l.size()
3
>>> l.add(7)
>>> l.size()
4
>>> 
"""

# String representation
"""
>>> l = LinkedList()
>>> l.add(7)
>>> l.add(3)
>>> l.add(6)
>>> l
[Head: 6]-> [3]-> [Tail: 7]
>>> 
"""

# Search function
"""
>>> l = LinkedList()
>>> l.add(10)
>>> l.add(6)
>>> l.add(3)
>>> n = l.search(6)
>>> n
<Node data: 6>
>>> l
[Head: 3]-> [6]-> [Tail: 10]
>>> 
"""

