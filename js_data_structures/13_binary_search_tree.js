/**
 * Tree and Binary Tree Data Structures
 * 
 * Tutorials:
 * - [Tutorial-1](https://www.youtube.com/watch?v=c-LEpmYikFY&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=65)
 * - [Tutorial-2](https://youtu.be/-ZMm8xX-Vrs?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP)
 * - [Tutorial-3](https://youtu.be/kIVkBsfB-SM?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP)
 * - [Tutorial-4](https://youtu.be/lml2E9SIJHo?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP)
 * - [Tutorial-5](https://youtu.be/n6_Ruq1qvjU?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP)
 * - [Tutorial-6](https://www.youtube.com/watch?v=H0i3gk1h0lI&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=71)
 * - [Tutorial-7](https://youtu.be/mrzE5SqzoQY?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP)
 * - [Tutorial-8](https://youtu.be/80GhW9X1MGI?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP)
 * 
 * Overview:
 * A tree is a hierarchical, non-linear data structure consisting of nodes connected by edges. Unlike linear data structures 
 * (arrays, linked lists, stacks, and queues), trees provide quicker and easier access to data due to their non-linear nature.
 * Trees do not contain loops or cycles.
 * 
 * Tree Usages:
 * - File systems for directory structures
 * - Family trees
 * - Organization charts
 * - Document Object Model (DOM)
 * - Chat bots
 * - Abstract syntax trees
 * 
 * Tree Structure:
 * 
 *                      A
 *                   /  |  \
 *                  B   C   D
 *                /  \
 *               E    F
 * 
 * Terminology:
 * - **Leaf Node**: A node without any child nodes (e.g., E, F, C, D)
 * - **Root Node**: A node without a parent node (e.g., A)
 * - **Siblings**: Nodes that share the same parent (e.g., E and F, C and D)
 * - **Ancestor**: A node that is an upper node in the hierarchy (e.g., A is an ancestor of E)
 * - **Path**: A sequence of nodes from one node to another (e.g., Path(A, E) is A-B-E)
 * - **Distance**: The number of edges in the path between two nodes (e.g., Distance between A and E is 2)
 * - **Degree**: The number of child nodes a node has (e.g., Degree of B is 2)
 * - **Depth**: The number of edges from the root to a node (e.g., Depth of E is 2, Depth of root node is always 0)
 * - **Height**: The number of edges in the longest path from a node to a leaf (e.g., Height of A is 2)
 * 
 * Types of Trees:
 * 1. **General Tree**: A tree where each node can have any number of children.
 * 2. **Binary Tree**: A tree where each node can have at most two children.
 * 
 * Binary Tree:
 * 
 *                  10
 *                /   \
 *               5     15
 *             /  \
 *            3    7
 * 
 * In a binary tree, each node can have a maximum of two child nodes, typically referred to as the left child and the right child.
 * 
 * Properties of Binary Trees:
 * - **Full Binary Tree**: Every node has 0 or 2 children.
 * - **Complete Binary Tree**: All levels are completely filled except possibly the last level, and the last level has all keys as left as possible.
 * - **Perfect Binary Tree**: All internal nodes have two children and all leaves are at the same level.
 * - **Balanced Binary Tree**: The height of the left and right subtrees of any node differ by at most one.
 * 
 * Binary Search Tree (BST):
 * A type of binary tree where the value of each left child node must be smaller than the parent node, and the value of each right child node must be greater than the parent node.
 * 
 * Operations:
 * - **Insertion**: Add a node to the tree. Start at the root and traverse the tree to find the correct location for the new node. O(log n) on average, O(n) in the worst case
 * - **Search**: Find a node given its value. Start at the root and traverse the tree, comparing the target value with each node's value. O(log n) on average, O(n) in the worst case
 * - **Depth-First Search (DFS)**: Traverse the tree by exploring as far as possible along each branch before backtracking. Includes in-order, pre-order, and post-order traversals. 
 * - **Breadth-First Search (BFS)**: Traverse the tree level by level, visiting all nodes at the present depth level before moving on to nodes at the next depth level. 
 * - **Deletion**: Remove a node given its value. This can be complex, involving three main cases: the node is a leaf, the node has one child, or the node has two children. O(log n) on average, O(n) in the worst case
 * 
 * 
 * Binary Search Tree (BST) Usage:
 * - **Searching**: Efficiently find values in a sorted order.
 * - **Sorting**: In-order traversal of a BST results in sorted order.
 * - **Implementing Abstract Data Types**: Such as lookup tables, sets, and priority queues.
 * 
 * Tree traversal
 * 
 *                  10
 *                /   \
 *               5     15
 *             /  \
 *            3    7
 * 
 * Visiting every node in the tree 
 * A hierarchical data structure like a tree can be traversed in different ways
 *      1. Depth first search (DFS)
 *      2. Breadth first search (BFS)
 * 
 * Depth first search(DFS)
 * The DFS algorithm start at the root node and explores as fas as possible along each branch before backtracking
 * Visit the root node, visit all the nodes in the left subtree and visit all the nodes in the right subtree
 * 
 * Depending on the order in which we do this, there can be three types of DFS traversals
 * DFS Variants:
 * - **In-order Traversal**: Visit the left subtree, the root (Read the data), then the right subtree. So the order will be 3, 5, 7, 10, 15
 * - **Pre-order Traversal**: Visit the root (Read the data), the left subtree, then the right subtree. So the order will be 10, 5, 3, 7, 15 in pre-order
 * - **Post-order Traversal**: Visit the left subtree, the right subtree, then the root (Read the data).
 * 
 * Breath First Search (BFS) Traversal
 * Explore all nodes at the present depth prior to moving on to the nodes at the next depth level. Usually the order is 10, 5, 15, 3, 7
 * 
 * Process:
 *      1. Create a queue
 *      2. Enqueue the root node
 *      3. As long as a node exist in the queue:
 *              a. Dequeue the node from the front
 *              b. Read the value of the node
 *              c. Enqueue the left child of the node if it is exists
 *              d. Enqueue the right child of the node if it is exists
 * 
 * Delete
 * Delete a node that is leaf node (No child of the node)
 * Delete a node that has one child node, in this case, remove the node and replace it with it's child
 * Delete a node that has two child node, in that case, copy the value of inorder successor and delete the in order successor
 */



class Node {
    // Constructor to create a new Node
    constructor(value) {
        this.value = value; // Value of the node
        this.left = null; // Left child
        this.right = null; // Right child
    }
}

class BinarySearchTree {
    // Constructor to create an empty BST
    constructor() {
        this.root = null; // Root of the BST
    }

    // Check if the tree is empty
    isEmpty() {
        return this.root === null; // Returns true if the tree is empty
    }

    // Insert a new node into the tree
    insert(value) {
        const newNode = new Node(value); // Create a new node
        if (this.isEmpty()) {
            this.root = newNode; // If tree is empty, set the root to the new node
        } else {
            this.insertNode(this.root, newNode); // Otherwise, insert the node at the correct position
        }
    }

    // Helper function to insert a node into the correct position
    insertNode(root, newNode) {
        if (newNode.value < root.value) { // Left child node must be smaller than the parent node
            if (root.left === null) {
                root.left = newNode; // Insert as the left child
            } else {
                this.insertNode(root.left, newNode); // Recur down the left subtree
            }
        } else { // Right child node must be greater than or equal to the parent node
            if (root.right === null) {
                root.right = newNode; // Insert as the right child
            } else {
                this.insertNode(root.right, newNode); // Recur down the right subtree
            }
        }
    }

    // Search for a node with a given value
    search(root, value) {
        if (!root) return false; // Base case: the node is not found

        if (value === root.value) return true; // Node is found
        if (value < root.value) {
            return this.search(root.left, value); // Search in the left subtree
        } else {
            return this.search(root.right, value); // Search in the right subtree
        }
    }

    // Pre-order traversal: Root -> Left -> Right
    preOrder(root) {
        if (root) {
            console.log(root.value); // Visit the root node
            this.preOrder(root.left); // Traverse the left subtree
            this.preOrder(root.right); // Traverse the right subtree
        }
    }

    // In-order traversal: Left -> Root -> Right
    inOrder(root) {
        if (root) {
            this.inOrder(root.left); // Traverse the left subtree
            console.log(root.value); // Visit the root node
            this.inOrder(root.right); // Traverse the right subtree
        }
    }

    // Post-order traversal: Left -> Right -> Root
    postOrder(root) {
        if (root) {
            this.postOrder(root.left); // Traverse the left subtree
            this.postOrder(root.right); // Traverse the right subtree
            console.log(root.value); // Visit the root node
        }
    }

    // Level-order traversal (BFS)
    levelOrder() {
        const queue = [];
        queue.push(this.root); // Start with the root node
        while (queue.length) {
            let currentNode = queue.shift(); // Dequeue the current node
            console.log(currentNode.value); // Visit the current node
            if (currentNode.left) {
                queue.push(currentNode.left); // Enqueue the left child
            }
            if (currentNode.right) {
                queue.push(currentNode.right); // Enqueue the right child
            }
        }
    }

    // Find the minimum value node in the tree
    min(root) {
        if (!root.left) {
            return root.value; // The minimum value is found
        } else {
            return this.min(root.left); // Keep traversing the left subtree
        }
    }

    // Find the maximum value node in the tree
    max(root) {
        if (!root.right) {
            return root.value; // The maximum value is found
        } else {
            return this.max(root.right); // Keep traversing the right subtree
        }
    }

    // Delete a node from the tree
    delete(value) {
        this.root = this.deleteNode(this.root, value); // Start the deletion process from the root
    }

    // Helper function to delete a node
    deleteNode(root, value) {
        if (root === null) return root; // Base case: the node is not found

        if (value < root.value) {
            root.left = this.deleteNode(root.left, value); // Traverse the left subtree
        } else if (value > root.value) {
            root.right = this.deleteNode(root.right, value); // Traverse the right subtree
        } else {
            // Node with only one child or no child
            if (!root.left) {
                return root.right;
            } else if (!root.right) {
                return root.left;
            }
            // Node with two children: Get the inorder successor (smallest in the right subtree)
            root.value = this.min(root.right);
            // Delete the inorder successor
            root.right = this.deleteNode(root.right, root.value);
        }
        return root;
    }
}

// Example usage:
const bst = new BinarySearchTree();
console.log("Is tree empty?", bst.isEmpty()); // true

bst.insert(10);
bst.insert(5);
bst.insert(15);
bst.insert(3);

console.log("Is 5 exist in the tree?", bst.search(bst.root, 5)); // true
console.log("Is 20 exist in the tree?", bst.search(bst.root, 20)); // false

console.log("===== Pre Order =====");
bst.preOrder(bst.root); // 10, 5, 3, 15

console.log("===== In Order =====");
bst.inOrder(bst.root); // 3, 5, 10, 15

console.log("===== Post Order =====");
bst.postOrder(bst.root); // 3, 5, 15, 10

console.log("===== Level Order =====");
bst.levelOrder(); // 10, 5, 15, 3

console.log("Minimum node:", bst.min(bst.root)); // 3
console.log("Maximum node:", bst.max(bst.root)); // 15

console.log("===== Delete =====");
bst.delete(15);
bst.levelOrder(); // 10, 5, 3