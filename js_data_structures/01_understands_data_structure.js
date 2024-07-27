/**
 * Tutorial: https://www.youtube.com/watch?v=poGEVboh9Rw&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=36
 * 
 * Data Structures in JavaScript
 * =============================
 * 
 * Understanding and implementing data structures is crucial for building efficient applications.
 * 
 * Key Concepts
 * ------------
 * 1. **Understanding Over Memorization**:
 *    - Focus on understanding the concepts rather than memorizing the implementations.
 * 
 * What is a Data Structure?
 * -------------------------
 * - A data structure is a way to store and organize data so that it can be used efficiently.
 * - It is a collection of data values, the relationships among them, and the functions or operations that can be applied to that data.
 * 
 * Why Learn Data Structures?
 * --------------------------
 * - Almost every application we build involves data that needs to be modeled in a certain way.
 * - Efficient data management requires the selection of the right data structure.
 * - The difference between a function taking milliseconds vs. seconds or even minutes can come down to the choice of data structure.
 * - Learning about data structures helps solve problems more efficiently in terms of time and space.
 * - It provides a deeper understanding of concepts you're already familiar with, such as:
 *   - DOM manipulation (Tree data structure)
 *   - Browser history (Stack data structure)
 *   - Operating System job scheduling (Queue data structure)
 * 
 * Built-in Data Structures in JavaScript
 * --------------------------------------
 * 1. Arrays
 * 2. Objects
 * 3. Sets
 * 4. Maps
 * 
 * Custom Data Structures
 * ----------------------
 * 1. Stacks
 * 2. Queues
 * 3. Circular Queues
 * 4. Linked Lists
 * 5. Hash Tables
 * 6. Trees
 * 7. Graphs
 * 
 * Examples and Implementations
 * ----------------------------
 * Below are brief descriptions and simple implementations of some custom data structures.
 * 
 * 1. Stack
 * --------
 * A stack is a collection of elements that follows the Last In, First Out (LIFO) principle.
 * 
 * Example:
 * ```javascript
 * class Stack {
 *     constructor() {
 *         this.items = [];
 *     }
 *     push(element) {
 *         this.items.push(element);
 *     }
 *     pop() {
 *         if (this.items.length === 0) return "Underflow";
 *         return this.items.pop();
 *     }
 *     peek() {
 *         return this.items[this.items.length - 1];
 *     }
 *     isEmpty() {
 *         return this.items.length === 0;
 *     }
 * }
 * ```
 * 
 * 2. Queue
 * --------
 * A queue is a collection of elements that follows the First In, First Out (FIFO) principle.
 * 
 * Example:
 * ```javascript
 * class Queue {
 *     constructor() {
 *         this.items = [];
 *     }
 *     enqueue(element) {
 *         this.items.push(element);
 *     }
 *     dequeue() {
 *         if (this.items.length === 0) return "Underflow";
 *         return this.items.shift();
 *     }
 *     front() {
 *         if (this.items.length === 0) return "No elements in Queue";
 *         return this.items[0];
 *     }
 *     isEmpty() {
 *         return this.items.length === 0;
 *     }
 * }
 * ```
 * 
 * 3. Linked List
 * --------------
 * A linked list is a linear data structure where each element is a separate object, called a node. Each node contains data and a reference (link) to the next node in the sequence.
 * 
 * Example:
 * ```javascript
 * class Node {
 *     constructor(data, next = null) {
 *         this.data = data;
 *         this.next = next;
 *     }
 * }
 * class LinkedList {
 *     constructor() {
 *         this.head = null;
 *     }
 *     insertFirst(data) {
 *         this.head = new Node(data, this.head);
 *     }
 *     size() {
 *         let count = 0;
 *         let node = this.head;
 *         while (node) {
 *             count++;
 *             node = node.next;
 *         }
 *         return count;
 *     }
 * }
 * ```
 * 
 * Additional Data Structures
 * --------------------------
 * - **Circular Queues**: A queue where the last position is connected back to the first position to make a circle.
 * - **Hash Tables**: A data structure that implements an associative array, a structure that can map keys to values.
 * - **Trees**: A hierarchical structure where data is organized in a tree-like format.
 * - **Graphs**: A collection of nodes connected by edges, used to represent networks.
 * 
 * Learning and implementing these data structures will enable you to build more efficient and scalable applications.
 */
