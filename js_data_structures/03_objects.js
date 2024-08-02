/**
 * Tutorial: https://youtu.be/1c9CArj66mU?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * Arrays in JavaScript are ordered collections of elements, allowing you to store multiple values 
 * in a single variable. Arrays are iterable, which means you can use loops and array methods to 
 * traverse and manipulate them.
 * 
 * Key Characteristics:
 * - Ordered Collection: Arrays maintain the order of elements based on their index.
 * - Index-Based Access: Elements are accessed using zero-based indexing.
 * - Dynamic Size: Arrays can dynamically grow or shrink in size.
 * 
 * Common Array Operations and Time Complexity:
 * 
 * 1. Insertion
 * - Description: Adding new elements to the array.
 * - Methods:
 *   - `push(element)`: Adds an element to the end of the array.
 *   - `unshift(element)`: Adds an element to the beginning of the array.
 *   - `splice(index, 0, element)`: Inserts an element at a specified index.
 * - Time Complexity:
 *   - `push()`: O(1) - Constant time for adding an element at the end.
 *   - `unshift()`: O(n) - Linear time as it shifts all elements to the right.
 *   - `splice()`: O(n) - Linear time due to shifting elements after the insertion point.
 * 
 * 2. Deletion
 * - Description: Removing elements from the array.
 * - Methods:
 *   - `pop()`: Removes the last element of the array.
 *   - `shift()`: Removes the first element of the array.
 *   - `splice(index, 1)`: Removes an element at a specified index.
 * - Time Complexity:
 *   - `pop()`: O(1) - Constant time for removing the last element.
 *   - `shift()`: O(n) - Linear time as it shifts all elements to the left.
 *   - `splice()`: O(n) - Linear time due to shifting elements after the removal point.
 * 
 * 3. Access
 * - Description: Retrieving elements by their index.
 * - Methods:
 *   - Direct index access (`array[index]`).
 * - Time Complexity:
 *   - Access: O(1) - Constant time for retrieving an element by index.
 * 
 * 4. Search
 * - Description: Finding whether a specific element exists in the array.
 * - Methods:
 *   - `indexOf(element)`: Returns the index of the first occurrence of the element.
 *   - `includes(element)`: Checks if the element exists in the array.
 * - Time Complexity:
 *   - `indexOf()`: O(n) - Linear time in the worst case (when the element is at the end or not present).
 *   - `includes()`: O(n) - Linear time due to the need to check each element.
 * 
 * 5. Iteration
 * - Description: Looping through each element in the array.
 * - Methods:
 *   - `forEach(callback)`: Executes a callback function once for each array element.
 *   - `map(callback)`: Creates a new array with the results of calling a callback function on each element.
 * - Time Complexity:
 *   - `forEach()`: O(n) - Linear time, iterating through all elements.
 *   - `map()`: O(n) - Linear time, as it processes each element once.
 * 
 * 6. Transformation
 * - Description: Creating a new array based on transformations.
 * - Methods:
 *   - `filter(callback)`: Creates a new array with all elements that pass the test implemented by the callback function.
 *   - `reduce(callback, initialValue)`: Applies a function against an accumulator and each element in the array to reduce it to a single value.
 * - Time Complexity:
 *   - `filter()`: O(n) - Linear time, as it evaluates each element once.
 *   - `reduce()`: O(n) - Linear time, as it processes each element in the array.
 * 
 * Summary of Big-O Notation for Array Operations:
 * - Insertion:
 *   - `push()`: O(1)
 *   - `unshift()`: O(n)
 *   - `splice()`: O(n)
 * - Deletion:
 *   - `pop()`: O(1)
 *   - `shift()`: O(n)
 *   - `splice()`: O(n)
 * - Access: O(1)
 * - Search:
 *   - `indexOf()`: O(n)
 *   - `includes()`: O(n)
 * - Iteration:
 *   - `forEach()`: O(n)
 *   - `map()`: O(n)
 * - Transformation:
 *   - `filter()`: O(n)
 *   - `reduce()`: O(n)
 */




const obj = {
    name: "Bruce",
    age: 25,
    "key-three": true,
    seeMyName: function(){
        console.log(this.name);
    }
};

obj.hobby = "Football";
delete obj.hobby;

console.log(obj);
console.log(obj.name); // Dot notation
console.log(obj['age']); // Bracket notation
console.log(obj['key-three']);
console.log(obj);
obj.seeMyName();

