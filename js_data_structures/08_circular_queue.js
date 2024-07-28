/**
 * Tutorial-1: https://youtu.be/ngNJps_RUg8?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * Tutorial-2: https://youtu.be/oIR_DOOOACk?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * Curcular Queue 
 * The size of the queue is fixed and a single block of memory is used as if the first element is connected to the last element.
 * Also refferred to as circular buffer or ring buffer and follows the FIFO principle.
 * A circular queue will reuse the empty block created during the dequeue operation.
 * When working with queue of fixed maximum size, a circular  queue is a great implementation choice.
 * 
 * The circular queue data structure supports the main operations
 *      Enqueue - Add an element to the rear/tail of the collection
 *      Dequeue - Remove an element from the front/head of the collection
 * 
 * Circular queue usage:
 *      Clock
 *      Streaming data
 *      Traffic Light
 */




class CircularQueue {
    constructor(capacity) {
        this.items = new Array(capacity);
        this.capacity = capacity;
        this.currLen = 0;
        this.rear = -1; // https://youtu.be/oIR_DOOOACk?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&t=218
        this.front = -1; // No position in the queue initially 03:07 - https://youtu.be/oIR_DOOOACk?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&t=187
    }

    isFull() {
        return this.currLen === this.capacity;
    }

    isEmpty() {
        return this.currLen === 0;
    }

    enqueue(element) {
        if (!this.isFull()) {
            this.rear = (this.rear + 1) % this.capacity;
            this.items[this.rear] = element;
            this.currLen++;
            if (this.front === -1) {
                this.front = this.rear;
            }
        }
    }


    dequeue() {
        if (this.isEmpty()) return null;

        const item = this.items[this.front];
        this.items[this.front] = null;
        this.front = (this.front + 1) % this.capacity;
        this.currLen--;
        if (this.isEmpty()) {
            this.front = -1;
            this.rear = -1;
        }

        return item;
    }

    peek() {
        if (!this.isEmpty()) return this.items[this.front];
        return null;
    }

    print() {
        if (this.isEmpty()) {
            console.log("Queue is empty...");
        } else {
            let i;
            let str = '';
            for (let i = this.front; i !== this.rear; i = (i + 1) % this.capacity) {
                str += this.items[i] + " ";
            }
            str += this.items[i];
            console.log(str);
        }
    }

}


const circularQueue = new CircularQueue(6);
console.log(circularQueue.isEmpty() ? "Queue is empty!" : "Queue is not empty!");
circularQueue.enqueue(10);
circularQueue.enqueue(20);
circularQueue.enqueue(30);
circularQueue.enqueue(40);
circularQueue.enqueue(50);
console.log(`Queue is full: ${circularQueue.isFull()}`);
circularQueue.print();
circularQueue.dequeue();
circularQueue.peek();
circularQueue.print();