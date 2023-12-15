# Binary Tree Algorithms

 - [YouTube Tutorial](https://www.youtube.com/watch?v=fAAZixBzIAI)
 - A binary tree is a hierarchical data structure in computer science that consists of nodes connected by edges. Each node in a binary tree has at most **two children**, which are referred to as the left child and the right child. 

 ![Tree Data Structure](tree_data_structure.jpg)

 - Tree contains many nodes
 - **Root** is a node that have no parent. All other nodes are descendants of the root.
 - Node: A fundamental part of a tree that contains data and may have references to its left and/or right children.
 - Parent: A node in a tree that has one or more child nodes.
 - Child: A node in a tree that has a parent node.
 - Leaf: A node in a tree that has no children, i.e., it is a node with zero out-degree.
 - Subtree: A tree formed by a node and its descendants.
 - Depth: The level or distance of a node from the root. The depth of the root is 0.
 - Height (or Depth): The length of the longest path from a node to a leaf. The height of a tree is the height of its root.
 - Rule-1: If we give more than 2 child that would be a tree but not a binary tree
 - Binary tree must have only one singe root
 - *[00:05:42]* Rule-2: Binary tree must have only **one path**, if there is more than one path it is no longer a binary tree
 - *[00:06:49]* If there is no node we should consider that empty tree as binary tree
 - *[00:14:20]* **Depth-First Search (DFS)** is a traversal algorithm commonly applied to binary trees. It explores as far as possible along one branch before backtracking. There are three main types of DFS traversal for binary trees: Inorder, Preorder, and Postorder. 
 - High-level summary of the DFS algorithm
    1. Start at the root node (or a specified starting node in a graph).
    2. Visit the current node.
    3. Recursively traverse the left subtree (or visit adjacent vertices in the case of a graph).
    4. Recursively traverse the right subtree (or visit remaining adjacent vertices).
    5. Continue this process until all nodes are visited.
 - In depth-first traversal, a **stack** is often used to keep **track of the nodes** that need to be visited. The stack stores the nodes that have been encountered but not yet fully processed. 

 - How stack is used in depth-first traversal
   1. Initialization: Start with an empty stack.
   2. Push the Root Node onto the Stack: Push the root node onto the stack to start the traversal.
   3. Pop and Process Nodes Until the Stack is Empty:
      - Pop a node from the stack.
      - Process the node (e.g., print its value or perform a specific operation).
      - Push its right child onto the stack (if it exists).
      - Push its left child onto the stack (if it exists).
   4. Repeat Until the Stack is Empty: Continue this process until the stack is empty.