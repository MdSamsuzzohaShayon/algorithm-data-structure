/**
 * Tutorial-1: https://www.youtube.com/watch?v=-0ZIresFUZI&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=59
 * Stack follows LIFO principle
 */

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;

    }

    isEmpty() {
        return this.size === 0;
    }

    getSize() {
        return this.size;
    }





    print() {
        if (this.isEmpty()) {
            console.log("List is empty!");
        } else {
            // Traverse the list
            let curr = this.head;
            let listValues = "";
            while (curr) {
                listValues += `${curr.value} `;
                curr = curr.next;
            }

            console.log(listValues);
        }
    }



    prepend(value) {
        const node = new Node(value);
        if(this.isEmpty()){
            this.head = node;
            this.tail = node;
        }else{
            node.next = this.head;
            this.head = node;
        }
        this.size++;
    }

    append(value) {
        const node = new Node(value);
        if(this.isEmpty()){
            this.head = node;
            this.tail = node;
        }else{
            this.tail.next = node;
            this.tail = node; 
        }
        this.size++;
    }

    removeFromFront(){
        if(this.isEmpty())return null;
        const value = this.head.value;
        this.head = this.head.next;
        this.size--;
        return value;
    }

    removeFromEnd(){
        if(this.isEmpty())return null;
        const value = this.tail.value;
        if(this.size === 1){
            this.head = null;
            this.tail = null;
        }else{
            let prev = this.head;
            while (prev.next !== this.tail) {
                prev = prev.next;
            }
            prev.next = null;
            this.tail = prev;
        }
        this.size--;
        return value
    }
}


// LIFO = Last In First Out
class LinkedListStack{
    constructor(){
        this.list = new LinkedList();
    }

    push(value){
        this.list.prepend(value);
    }
    pop(){
        this.list.removeFromFront();
    }
    peek(){
        return this.list.head.value;
    }
    isEmpty(){
        return this.list.isEmpty();
    }
    getSize(){
        return this.list.getSize();
    }
    print(){
        return this.list.print();
    }
}


const stack = new LinkedListStack();
stack.push(10);
stack.push(20);
stack.push(30); // inserted at the list, should be deleted first
stack.print();
stack.pop();
stack.print();
console.log(stack.peek());;