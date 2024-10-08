/**
 * Tutorial-1: https://www.youtube.com/watch?v=3OsxH-huRc4&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=47
 * Tutorial-2: https://youtu.be/Tggvw4QlA9U?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * Tutorial-3: https://youtu.be/A-9tzPuE1eA?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * Insert: https://www.youtube.com/watch?v=Sd9Nps5nAdU&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=52
 * Remove: https://www.youtube.com/watch?v=D_kWagEfcx8&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=53
 * Search: https://youtu.be/ZRIJuAIGJ4M?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * Tail O(1): https://youtu.be/sw7fCZeFTdc?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
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




// Node class represents each element in the LinkedList
class Node {
    constructor(value) {
        this.value = value; // Data of the node
        this.next = null;   // Pointer to the next node
    }
}

// LinkedList class to handle operations on the list
class LinkedList {
    constructor() {
        this.head = null;  // First node of the list
        this.size = 0;     // Size of the list
    }

    // Check if the list is empty
    // Time Complexity: O(1)
    // Space Complexity: O(1)
    isEmpty() {
        return this.size === 0;
    }

    // Get the size of the list
    // Time Complexity: O(1)
    // Space Complexity: O(1)
    getSize() {
        return this.size;
    }

    // Add an element at the beginning of the list
    // Time Complexity: O(1)
    // Space Complexity: O(1)
    prepend(value) {
        const node = new Node(value);
        if (this.isEmpty()) {
            this.head = node;
        } else {
            node.next = this.head;
            this.head = node;
        }
        this.size++;
    }

    // Add an element at the end of the list
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    append(value) {
        const node = new Node(value);
        if (this.isEmpty()) {
            this.head = node;
        } else {
            let prev = this.head;
            while (prev.next) {
                prev = prev.next;
            }
            prev.next = node;
        }
        this.size++;
    }

    // Insert an element at a specific index
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    insert(value, index) {
        if (index < 0 || index > this.size) return;
        if (index === 0) {
            this.prepend(value);
        } else {
            const node = new Node(value);
            let prev = this.head;
            for (let i = 0; i < index - 1; i++) {
                prev = prev.next;
            }
            node.next = prev.next;
            prev.next = node;
            this.size++;
        }
    }

    // Remove an element from a specific index
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    removeFrom(index) {
        if (index < 0 || index >= this.size) return null;
        let removeNode;
        if (index === 0) {
            removeNode = this.head;
            this.head = this.head.next;
        } else {
            let prev = this.head;
            for (let i = 0; i < index - 1; i++) {
                prev = prev.next;
            }
            removeNode = prev.next;
            prev.next = removeNode.next;
        }
        this.size--;
        return removeNode.value;
    }

    // Remove an element by value
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    removeValue(value) {
        if (this.isEmpty()) return null;
        if (this.head.value === value) {
            this.head = this.head.next;
            this.size--;
            return value;
        } else {
            let prev = this.head;
            while (prev.next && prev.next.value !== value) {
                prev = prev.next;
            }
            if (prev.next) {
                const removedNode = prev.next;
                prev.next = removedNode.next;
                this.size--;
                return value;
            }
            return null;
        }
    }

    // Search for an element by value
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    search(value) {
        if (this.isEmpty()) return -1;
        let i = 0;
        let curr = this.head;
        while (curr) {
            if (curr.value === value) return i;
            curr = curr.next;
            i++;
        }
        return -1;
    }

    // Reverse the linked list
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    reverse() {
        let curr = this.head;  // Initialize current node to head
        let prev = null;       // Initialize previous node to null

        // Traverse through the list
        while (curr) {
            let next = curr.next;  // Store the next node
            curr.next = prev;      // Reverse the current node's pointer
            prev = curr;           // Move the previous node to the current node
            curr = next;           // Move the current node to the next node
        }

        this.head = prev;  // After the loop, prev will be the new head of the reversed list

        /**
         * Step-by-Step Explanation:
         * 
         * Initialize Current and Previous Pointers:
         *       curr is initialized to this.head to start from the beginning of the list.
         *       prev is initialized to null because the new end of the list (the old head) will point to null.
         * 
         * Traverse the List:
         * The loop runs as long as curr is not null.
         * Inside the loop:
         *       next stores the next node (curr.next), preserving the link to the rest of the list.
         *       curr.next is set to prev, reversing the direction of the current node’s pointer.
         *       prev is updated to the current node (curr), moving the previous pointer forward.
         *       curr is updated to the next node (next), moving the current pointer forward.
         * 
         * Update Head:
         *       After the loop completes, prev will point to the new head of the reversed list.
         *       this.head is updated to prev, finalizing the reversal of the list.
         */
    }

    // Print the elements of the list
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    print() {
        if (this.isEmpty()) {
            console.log("List is empty!");
        } else {
            let curr = this.head;
            let listValues = "";
            while (curr) {
                listValues += `${curr.value} `;
                curr = curr.next;
            }
            console.log(listValues);
        }
    }
}

// Example usage of LinkedList
const list = new LinkedList();
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
list.insert(35, 3);
console.log("Search index: ", list.search(35));
console.log("Search index: ", list.search(36));
list.print();
list.removeFrom(0);
list.removeFrom(1);
list.print();
console.log("Removed value: ", list.removeValue(20));
list.print();
console.log("Removed value: ", list.removeValue(40));
console.log("Removed value: ", list.removeValue(35));
list.print();
list.append(5);
list.append(15);
list.append(25);
list.append(35);
list.append(45);
list.print();
list.reverse();
list.print();



console.log("======================  Linked List With Tail  =========================");
/**
 * Tutorial-1: https://youtu.be/sw7fCZeFTdc?si=eVTAs1ws5lnlJRYh
 * Tutorial-2: https://youtu.be/ADZfDxftXQ0?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 */

class TailLinkedList {
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
        if (this.isEmpty()) {
            this.head = node;
            this.tail = node;
        } else {
            node.next = this.head;
            this.head = node;
        }
        this.size++;
    }

    append(value) {
        const node = new Node(value);
        if (this.isEmpty()) {
            this.head = node;
            this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
        this.size++;
    }

    removeFromFront() {
        if (this.isEmpty()) return null;
        const value = this.head.value;
        this.head = this.head.next;
        this.size--;
        return value;
    }

    removeFromEnd() {
        if (this.isEmpty()) return null;
        const value = this.tail.value;
        if (this.size === 1) {
            this.head = null;
            this.tail = null;
        } else {
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


const tls = new TailLinkedList();
tls.append(1);
tls.append(2);
tls.append(3);
tls.prepend(4);

tls.print();
tls.removeFromFront();
tls.print();
tls.removeFromEnd();
tls.print();
