/**
 * Tutorial-1: https://www.youtube.com/watch?v=3OsxH-huRc4&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=47
 * Tutorial-2: https://youtu.be/Tggvw4QlA9U?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * Tutorial-3: https://youtu.be/A-9tzPuE1eA?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * A Linked list is a linear data structure that includes a series of connected nodes
 * Each node consists of a data value and a pointer that points to the next node
 * The list element can be easily inserted or removed without reallocation of reorganization of the entire structure
 * Random access of element is not feasiable and accessing an element has linear time complexity
 * 
 * The linked list data structure supports three main operations
 * Insertion - Add an element at the beginning, end or at a given index in the list
 * Deletion - to remove an item at given index or value
 * Search - to find an element given its value
 * 
 * Linked list usage
 * All application of both stacks and queues are applications of linked lists
 * image viewer
 * 
 */


class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}


class LinkedList{
    constructor(){
        this.head = null;
        this.size = 0;

    }

    isEmpty(){
        return this.size === 0;
    }

    getSize(){
        return this.size;
    }

    // Adding an element at the beginning of the list
    // Big-O  = O(1) Constant time complexity
    prepend(value){
        const node = new Node(value);
        if(this.isEmpty()){
            this.head = node;
        }else{
            node.next = this.head;
            this.head = node;
        }
        this.size++;
    }

    // Add element at the end of the list
    // Big-O  = O(n) Linear time complexity
    append(value){
        const node = new Node(value);
        if(this.isEmpty()){
            this.head = node;
        } else {
            let prev = this.head;

            // The while loop will stop when we reach last node since last node has null value for next pointer
            while(prev.next){
                prev = prev.next;
            }
            prev.next = node;
        }
        this.size++;
    }

    print(){
        if(this.isEmpty()){
            console.log("List is empty!");
        }else{
            // Traverse the list
            let curr = this.head;
            let listValues = "";
            while(curr){
               listValues += `${curr.value} ` ;
               curr = curr.next;
            }

            console.log(listValues);
        }
    }
}

const list  = new LinkedList();
list.print();
console.log("List is empty? ", list.isEmpty());
console.log("List size: ", list.getSize());
list.prepend(30);
list.print();
list.prepend(20);
list.prepend(10);
list.print();
list.append(40);
list.print();