/**
 * Tutorial: https://www.youtube.com/watch?v=ex8EHl5fq1o&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=42
 * The queue data structure is a sequential collection of elements that follows the principle of First In First out (FIFO)
 * First element inserted into the queue is first element to be removed
 * A queue of people. People enter the queue at one end (rear/tail) and leave the queue from the other end( front/head )
 * Queue is an abstract data type. It is defined by its behavior rather than being a mathematical model.
 * 
 * The queue data structure dsupports two main operations
 * Enqueue - Add an element to the rear/tail of the collection
 * Dequeue - Remove an element from the front/head of the collection
 * 
 * Queue usage
 * Printers - printing multiple documents
 * CPU - task scheduling
 * Callback queue in JavaScript runtime
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
