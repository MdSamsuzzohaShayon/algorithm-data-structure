/**
 * Tree and Binary Tree Data Structures
 * 
 * Tutorials:
 * - [Tutorial-1](https://www.youtube.com/watch?v=c-LEpmYikFY&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=65)
 * - [Tutorial-2](https://youtu.be/-ZMm8xX-Vrs?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP)
 * - [Tutorial-3](https://youtu.be/kIVkBsfB-SM?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP)
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
 * - **Insertion**: Add a node to the tree. Start at the root and traverse the tree to find the correct location for the new node.
 * - **Search**: Find a node given its value. Start at the root and traverse the tree, comparing the target value with each node's value.
 * - **Depth-First Search (DFS)**: Traverse the tree by exploring as far as possible along each branch before backtracking. Includes in-order, pre-order, and post-order traversals.
 * - **Breadth-First Search (BFS)**: Traverse the tree level by level, visiting all nodes at the present depth level before moving on to nodes at the next depth level.
 * - **Deletion**: Remove a node given its value. This can be complex, involving three main cases: the node is a leaf, the node has one child, or the node has two children.
 * 
 * DFS Variants:
 * - **In-order Traversal**: Visit the left subtree, the root, then the right subtree.
 * - **Pre-order Traversal**: Visit the root, the left subtree, then the right subtree.
 * - **Post-order Traversal**: Visit the left subtree, the right subtree, then the root.
 * 
 * Binary Search Tree (BST) Usage:
 * - **Searching**: Efficiently find values in a sorted order.
 * - **Sorting**: In-order traversal of a BST results in sorted order.
 * - **Implementing Abstract Data Types**: Such as lookup tables, sets, and priority queues.
 * 
 */





class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}


class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    isEmpty() {
        return this.root === null;
    }

    insertNode(root, node){
        if(node.value < root.value){ // Left child node must be smaller than the parent node
            if(root.left === null){
                root.left = node;
            }else{
                this.insertNode(root.left, node);
            }
        }else{
            if(root.right === null){
                root.right = node;
            }else{
                this.insertNode(root.right, node);
            }
        }
    }

    insert(value) {
        const node = new Node(value);
        if (this.isEmpty()) {
            this.root = node;
        }else{
            this.insertNode(this.root, node);
        }
    }
}


const bst = new BinarySearchTree()
console.log("IS tree empty?", bst.isEmpty());
bst.insert(10);
bst.insert(5);
bst.insert(15);