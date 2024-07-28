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



class Queue {
    constructor() {
        this.items = [];
    }


    enqueue(element) {
        this.items.push(element);
    }

    dequeue() {
        // It has linear time complpexity Big-O = O(n)
        return this.items.shift(); // remove item from the beginning of the array
    }

    isEmpty() {
        return this.items.length === 0;
    }

    peek() {
        if (!this.isEmpty()) return this.items[0];
        return null;
    }

    size() {
        return this.items.length;
    }

    print() {
        console.log(this.items.toString());
    }
}



const queue = new Queue();


console.log(queue.isEmpty() ? "Queue is empty!" : "Queue is not empty!");
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.enqueue(40);
console.log(`Queue size: ${queue.size()}`);
queue.print();
queue.dequeue();
queue.print();
console.log("Peek of the queue: ", queue.peek());



// Optimized - https://youtu.be/ba15sgOiAOg?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
class OptimizedQueue {
    constructor() {
        this.items = {};
        this.rear = 0;
        this.front = 0;
    }

    enqueue(element){
        this.items[this.rear] = element;
        this.rear++;
    }

    dequeue(){
        const item = this.items[this.front];
        delete this.items[this.front];
        this.front++;
        return item;
    }

    isEmpty(){
        return this.rear - this.front === 0;
    }

    peek(){
        return this.items[this.front];
    }

    size(){
       return this.rear - this.front; 
    }

    print(){
        console.log(this.items);
    }


}



console.log("===================OPTIMIZED QUEUE===================");
const optimizedQueue = new OptimizedQueue();
console.log(optimizedQueue.isEmpty() ? "Queue is empty!" : "Queue is not empty!");
optimizedQueue.enqueue(10);
optimizedQueue.enqueue(20);
optimizedQueue.enqueue(30);
optimizedQueue.enqueue(40);
console.log(`Queue size: ${optimizedQueue.size()}`);
optimizedQueue.print();
console.log("Dequeue from the list: ",optimizedQueue.dequeue());
optimizedQueue.print();
console.log("Peek of the queue: ", optimizedQueue.peek());

/**
 * Enqueue and dequeue has constant time complexity Big-O = O(1)
 */
