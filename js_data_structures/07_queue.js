/**
 * Tutorial: https://www.youtube.com/watch?v=ex8EHl5fq1o&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=42
 * 
 * ## Overview of the Queue Data Structure
 * The queue data structure is a sequential collection of elements that follows the principle of First In, First Out (FIFO). This means that the first element inserted into the queue is the first element to be removed.
 * Imagine a queue of people: people enter the queue at one end (rear/tail) and leave the queue from the other end (front/head). This visual helps illustrate the FIFO principle.
 * 
 * ## Characteristics of a Queue
 * - **Abstract Data Type**: A queue is defined by its behavior rather than its implementation. It focuses on the operations it supports and the order in which operations are performed.
 * 
 * ## Primary Operations
 * 
 * A queue supports two main operations:
 * 1. **Enqueue**: Adds an element to the rear/tail of the queue.
 * 2. **Dequeue**: Removes an element from the front/head of the queue.
 * 
 * ## Real-Life Examples and Use Cases
 * - **Printers**: When printing multiple documents, they are added to a print queue. The first document sent to the printer is the first one printed.
 * - **CPU Task Scheduling**: Operating systems use queues to manage tasks. Processes are added to the CPU queue and are executed in the order they arrive.
 * - **Callback Queue in JavaScript Runtime**: In JavaScript, the event loop uses a callback queue to manage asynchronous operations. Callbacks are queued and executed in the order they are received.
 * - **Customer Service Lines**: In customer service scenarios, people line up in a queue. The first person in line is the first to be served.
 * - **Ticketing Systems**: When buying tickets (for movies, concerts, etc.), people are often placed in a virtual queue. The first person to enter the queue is the first to get their tickets processed.
 * 
 * ## Summary
 * Understanding queues and their operations is crucial for solving problems related to data management and process scheduling. Queues are widely used in various real-life and application scenarios, making them an essential data structure to learn.
 */


// Standard Queue Implementation
class Queue {
    constructor() {
        this.items = [];
    }

    // Add an element to the end of the queue
    // Time Complexity: O(1), Space Complexity: O(1)
    enqueue(element) {
        this.items.push(element);
    }

    // Remove and return the front element of the queue
    // Time Complexity: O(n), Space Complexity: O(1)
    dequeue() {
        return this.items.shift(); // Linear time complexity due to array shift
    }

    // Check if the queue is empty
    // Time Complexity: O(1), Space Complexity: O(1)
    isEmpty() {
        return this.items.length === 0;
    }

    // Return the front element of the queue without removing it
    // Time Complexity: O(1), Space Complexity: O(1)
    peek() {
        return !this.isEmpty() ? this.items[0] : null;
    }

    // Return the number of elements in the queue
    // Time Complexity: O(1), Space Complexity: O(1)
    size() {
        return this.items.length;
    }

    // Print all elements in the queue
    // Time Complexity: O(n), Space Complexity: O(1)
    print() {
        console.log(this.items.toString());
    }
}

// Example usage of Queue
const queue = new Queue();

console.log(queue.isEmpty() ? "Queue is empty!" : "Queue is not empty!"); // Queue is empty!
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.enqueue(40);
console.log(`Queue size: ${queue.size()}`); // Queue size: 4
queue.print(); // 10,20,30,40
queue.dequeue(); // Removes 10
queue.print(); // 20,30,40
console.log("Peek of the queue: ", queue.peek()); // Peek of the queue:  20

// Optimized Queue Implementation
class OptimizedQueue {
    constructor() {
        this.items = {};
        this.rear = 0;
        this.front = 0;
    }

    // Add an element to the end of the queue
    // Time Complexity: O(1), Space Complexity: O(1)
    enqueue(element) {
        this.items[this.rear] = element;
        this.rear++;
    }

    // Remove and return the front element of the queue
    // Time Complexity: O(1), Space Complexity: O(1)
    dequeue() {
        if (this.isEmpty()) return undefined;
        const item = this.items[this.front];
        delete this.items[this.front];
        this.front++;
        return item;
    }

    // Check if the queue is empty
    // Time Complexity: O(1), Space Complexity: O(1)
    isEmpty() {
        return this.rear - this.front === 0;
    }

    // Return the front element of the queue without removing it
    // Time Complexity: O(1), Space Complexity: O(1)
    peek() {
        return this.isEmpty() ? undefined : this.items[this.front];
    }

    // Return the number of elements in the queue
    // Time Complexity: O(1), Space Complexity: O(1)
    size() {
        return this.rear - this.front;
    }

    // Print all elements in the queue
    // Time Complexity: O(n), Space Complexity: O(n)
    print() {
        console.log(this.items);
    }
}

// Example usage of OptimizedQueue
console.log("===================OPTIMIZED QUEUE===================");
const optimizedQueue = new OptimizedQueue();

console.log(optimizedQueue.isEmpty() ? "Queue is empty!" : "Queue is not empty!"); // Queue is empty!
optimizedQueue.enqueue(10);
optimizedQueue.enqueue(20);
optimizedQueue.enqueue(30);
optimizedQueue.enqueue(40);
console.log(`Queue size: ${optimizedQueue.size()}`); // Queue size: 4
optimizedQueue.print(); // { '0': 10, '1': 20, '2': 30, '3': 40 }
console.log("Dequeue from the list: ", optimizedQueue.dequeue()); // Dequeue from the list: 10
optimizedQueue.print(); // { '1': 20, '2': 30, '3': 40 }
console.log("Peek of the queue: ", optimizedQueue.peek()); // Peek of the queue: 20

/**
 * Enqueue and dequeue in OptimizedQueue have constant time complexity Big-O = O(1)
 */
