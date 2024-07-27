/**
 * Tutorial: https://youtu.be/vfPd6_H7W4Q?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * Set in JavaScript
 * =================
 * A Set is a data structure that can hold a collection of unique values. 
 * A Set can contain a mix of different data types, including strings, booleans, numbers, and objects.
 * 
 * Key Characteristics of Sets
 * ---------------------------
 * 1. Uniqueness:
 *    - All values in a Set must be unique.
 * 
 * 2. Mixed Data Types:
 *    - Sets can hold a variety of data types simultaneously.
 *    - For example, a Set can contain a mix of strings, numbers, and objects.
 * 
 * 3. Dynamic Size:
 *    - Sets are dynamically sized; you do not need to declare the size of a Set before creating it.
 * 
 * 4. Insertion Order:
 *    - Sets do not maintain insertion order.
 * 
 * 5. Iterables:
 *    - Sets are iterables and can be used with a for-of loop.
 * 
 * Basic Operations
 * ----------------
 * 1. Creating a Set:
 *    let mySet = new Set();
 * 
 * 2. Adding values:
 *    mySet.add(1);
 *    mySet.add('hello');
 *    mySet.add({ key: 'value' });
 * 
 * 3. Checking for a value:
 *    mySet.has(1); // Returns true if 1 is in the Set
 * 
 * 4. Deleting a value:
 *    mySet.delete('hello'); // Removes 'hello' from the Set
 * 
 * 5. Getting the size of the Set:
 *    mySet.size; // Returns the number of elements in the Set
 * 
 * 6. Iterating over a Set:
 *    for (let value of mySet) {
 *        console.log(value);
 *    }
 * 
 * Set vs Array
 * ------------
 * 1. Duplicate Values:
 *    - Arrays can contain duplicate values.
 *    - Sets cannot contain duplicate values.
 * 
 * 2. Insertion Order:
 *    - Arrays maintain insertion order.
 *    - Sets do not maintain insertion order.
 * 
 * 3. Performance:
 *    - Searching and deleting an element in a Set is faster compared to an Array.
 * 
 * Examples
 * --------
 * Example of Set Operations:
 * 
 * let mySet = new Set();
 * mySet.add(1);
 * mySet.add('hello');
 * mySet.add({ key: 'value' });
 * mySet.add(1); // Duplicate value, will not be added
 * 
 * console.log(mySet.has(1)); // Output: true
 * console.log(mySet.size); // Output: 3
 * 
 * mySet.delete('hello');
 * console.log(mySet.size); // Output: 2
 * 
 * for (let value of mySet) {
 *     console.log(value);
 * }
 * // Output:
 * // 1
 * // { key: 'value' }
 * 
 * Example of Array Operations:
 * 
 * let myArray = [1, 2, 2, 3, 'hello'];
 * console.log(myArray.includes(2)); // Output: true
 * console.log(myArray.length); // Output: 5
 * 
 * myArray.splice(myArray.indexOf('hello'), 1); // Remove 'hello'
 * console.log(myArray.length); // Output: 4
 * 
 * for (let value of myArray) {
 *     console.log(value);
 * }
 * // Output:
 * // 1
 * // 2
 * // 2
 * // 3
 */



const nums = new Set([1, 2, 3]);
nums.add(4);
nums.add(5);
nums.delete(3);
console.log(nums.has(4));
for (const item of nums) {
    console.log(item);    
}
nums.clear();
console.log({nums});