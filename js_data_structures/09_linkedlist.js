/**
 * Tutorial-1: https://www.youtube.com/watch?v=3OsxH-huRc4&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=47
 * Tutorial-2: https://youtu.be/Tggvw4QlA9U?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
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
}

const list  = new LinkedList();
console.log("List is empty? ", list.isEmpty());
console.log("List size: ", list.getSize());