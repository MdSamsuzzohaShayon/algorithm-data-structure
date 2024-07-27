/**
 * Tutorial-1: https://youtu.be/a1fyufVlLmk?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * The stack data structure is a sequential collection of elements that follows the principle of Last in First Out (LIFO)
 * The last element inserted into the stack is first element to be removed
 * A stack of plates. The last plate placed on top of the stack is also the first plate removed from the stack.
 * Stack is an abstract data type. It is defined by its behavior rather than being a mathematical model
 * 
 * The stack data structure supprts two main operations
 * Push - shich add an element to the collection
 * Pop - which remove the most recently added element from the collection
 * 
 * Stack Usage:
 * Browser history tracking
 * undo Operation when typing
 * Expression conversations
 * Call stack in JavaScript runtime
 */


/**
 * Tutorial-2: https://www.youtube.com/watch?v=wtynhUwS5hI
 * Instead of using JS push and pop method of an array we are going to use our own data structure
 * 
 */

class Stack{
    constructor(){
        this.items = [];
        this.count = 0;
    }

    // Add element to the top of the stack
    push(element){
        this.items[this.count] = element;
        this.count += 1;
        console.log(`${element} added to ${this.count}`);
        return this.count - 1;
    }

    // Return and remove the top element in the stack
    // Return undefined if stack is empty
    pop(){
        if (this.count === 0) return undefined;
        let deletedItem = this.items[this.count - 1];
        this.count -= 1;
        console.log(`${deletedItem} removed`);
        return deletedItem;
    }

    // Check top element in the stack
    peek(){
        console.log(`Top element is ${this.items[this.count - 1]}`);
        return this.items[this.count - 1];
    }

    isEmpty(){
        console.log(this.count === 0 ? `Stack is empty` : "Stack is not empty");
        return this.count === 0;
    }
    size(){
        console.log(`${this.count} elements in the stack`);
        return this.count;
    }

    print(){
        let str = '';
        for (let i = 0; i < this.count; i++) {
            str += this.items[i] + " "
        }
        return str;
    }

    clear(){
        this.items = [];
        this.count = 0;
        console.log('Stack cleared...');;
        return this.items;
    }

}

const stack  = new Stack();

stack.isEmpty();

stack.push(100);
stack.push(200);
stack.push(300);

console.log(stack.print());
stack.isEmpty();
stack.peek();

stack.size();

stack.pop();
stack.pop();

stack.size();
stack.isEmpty();

stack.clear();
stack.isEmpty();