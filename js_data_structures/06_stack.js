/**
 * Tutorial-1: https://youtu.be/a1fyufVlLmk?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * ## Overview of the Stack Data Structure
 * The stack data structure is a sequential collection of elements that follows the principle of Last In, First Out (LIFO). This means that the last element inserted into the stack is the first element to be removed.
 * Visualize a stack of plates: the last plate placed on top of the stack is the first plate removed. This illustrates the LIFO principle.
 * 
 * ## Characteristics of a Stack
 * - **Abstract Data Type**: A stack is defined by its behavior rather than its implementation. It focuses on the operations it supports and the order in which operations are performed.
 * 
 * ## Primary Operations
 * A stack supports two main operations:
 * 1. **Push**: Adds an element to the top of the stack.
 * 2. **Pop**: Removes the most recently added element from the top of the stack.
 * 
 * ## Real-Life Examples and Use Cases
 * - **Browser History Tracking**: When navigating through web pages, your browser maintains a stack of visited pages. The most recent page visited is on top, and pressing the "Back" button takes you to the previous page.
 * - **Undo Operation**: Applications like text editors use a stack to keep track of actions. When you perform an action and then use the "Undo" button, the most recent action is reversed first.
 * - **Expression Evaluation**: In mathematical and logical expressions, stacks are used to evaluate expressions, especially in converting infix expressions to postfix (or reverse Polish notation) and evaluating them.
 * - **Call Stack in JavaScript Runtime**: In programming, the call stack keeps track of function calls. When a function is called, it is added to the stack, and once it completes, it is removed, returning control to the previous function.
 * - **Plate Stack Example**: Similar to a stack of plates in a cafeteria. Plates are added to the top of the stack and removed from the top, ensuring that the plate added most recently is the first one to be taken off.
 * 
 * ## Summary
 * Understanding stacks and their operations is crucial for solving problems related to data management and algorithm design. Stacks are versatile and are used in various real-life and application scenarios.
 */

/**
 * Tutorial-2: https://www.youtube.com/watch?v=wtynhUwS5hI
 * 
 * ## Custom Stack Implementation
 * Instead of using the built-in JavaScript array methods `push` and `pop`, we will create our own stack data structure. This allows for greater control and understanding of how the stack operates under the hood.
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