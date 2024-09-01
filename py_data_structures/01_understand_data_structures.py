"""
Tutorial-1: https://youtu.be/VAt2mR7gY0k
Tutorial-2: https://youtu.be/oz9cEqFynHU

A data structure is a way to organize information
A algorithm is a way to process information to reach an end goal


Data Structures in Python
========================

This file provides a detailed theoretical explanation of common data structures, their real-world applications, and common interview questions with answers.

1. Arrays
2. Linked Lists
3. Stacks
4. Queues
5. Trees
6. Graphs
7. Hash Tables
"""


# 1. Arrays
#  are collections of elements stored in contiguous memory locations. Each element can be accessed directly via its index.
# Real-world Application: A typical use of an array is to store a list of student grades or IDs.
# For example, you might use an array to keep track of monthly sales figures where each element represents a month's total sales.
# Advantages: Simple and fast access to elements using indices.
# Disadvantages: Fixed size and inefficient insertions or deletions, as elements need to be shifted.

# Interview Question:
# Q: How do you find the maximum value in an array?
# A: Iterate through the array and keep track of the maximum value encountered. This is an O(n) operation where n is the number of elements.

# 2. Linked Lists
# Linked Lists are collections of nodes where each node contains data and a reference (or link) to the next node in the sequence.
# Real-world Application: Linked lists are useful for implementing dynamic data structures like queues and stacks.
# For example, a linked list can represent a playlist where each song points to the next one.
# Advantages: Efficient insertions and deletions at both ends.
# Disadvantages: O(n) time complexity for accessing elements and additional memory usage for storing pointers.

# Interview Question:
# Q: What is the time complexity for inserting a new element in a linked list?
# A: Inserting an element at the beginning of a linked list is O(1). Inserting at the end requires O(n) time if the list is not doubly linked and there’s no tail pointer.

# 3. Stacks
# Stacks are collections of elements that follow the Last In, First Out (LIFO) principle. You can only add or remove elements from the top of the stack.
# Real-world Application: A stack is used in web browsers to manage the history of visited pages. Each new page is pushed onto the stack, and going back pops the top page.
# Advantages: Simple and efficient for problems where you need to reverse operations or manage nested structures.
# Disadvantages: Limited access to elements (only the top can be accessed).

# Interview Question:
# Q: How would you check for balanced parentheses in an expression using a stack?
# A: Use a stack to keep track of opening parentheses. For each closing parenthesis encountered, check if it matches the top of the stack. If it matches, pop the stack; if not, the expression is unbalanced.

# 4. Queues
# Queues are collections of elements that follow the First In, First Out (FIFO) principle. Elements are added to the rear and removed from the front.
# Real-world Application: Queues are used in print spooling where print jobs are processed in the order they are received.
# Advantages: Useful for scenarios where order of processing needs to be maintained.
# Disadvantages: Accessing elements other than the front or rear is inefficient.

# Interview Question: Q: What is a circular queue and how does it differ from a regular queue? A: A circular queue uses a circular buffer to efficiently use space and avoid the problem of running
# out of space due to unused slots. When the end of the buffer is reached, it wraps around to the beginning.

# 5. Trees
# Trees are hierarchical structures with a root node and child nodes, where each child node can have its own children. They are used to represent hierarchical data.
# Real-world Application: A file system on a computer is a tree structure where folders can contain files or other folders.
# Advantages: Efficient for hierarchical data and operations like searching, insertion, and deletion.
# Disadvantages: More complex to implement compared to arrays and linked lists.

# Interview Question:
# Q: What is the time complexity for searching in a balanced binary search tree?
# A: The time complexity for searching in a balanced binary search tree is O(log n), where n is the number of nodes.

# 6. Graphs
# Graphs are collections of nodes (vertices) connected by edges. They can represent various relationships and are used in network modeling.
# Real-world Application: Graphs are used to model social networks where users (nodes) are connected by friendships (edges).
# Advantages: Flexible for modeling complex relationships and networks.
# Disadvantages: Can be complex to traverse and manage, especially if the graph is large.

# Interview Question:
# Q: What is the difference between directed and undirected graphs?
# A: In a directed graph, edges have a direction (from one vertex to another), while in an undirected graph, edges do not have a direction and represent a bidirectional relationship.

# 7. Hash Tables
# Hash Tables store key-value pairs and use a hash function to compute an index into an array of buckets or slots. They provide fast access based on keys.
# Real-world Application: Hash tables are used in implementations of associative arrays, such as a dictionary or phone book, where names (keys) are mapped to phone numbers (values).
# Advantages: Efficient average-case time complexity for search, insert, and delete operations.
# Disadvantages: Poor performance in the worst-case scenario (e.g., with many collisions) and requires a good hash function.

# Interview Question:
# Q: How do you handle collisions in a hash table?
# A: Common methods include chaining (using linked lists to store multiple elements in the same slot) and open addressing (probing for the next available slot).

"""
This document provides a theoretical overview of essential data structures, their real-world applications, and answers to common interview questions. 
Understanding these concepts is crucial for effective problem-solving and algorithm design.
"""
