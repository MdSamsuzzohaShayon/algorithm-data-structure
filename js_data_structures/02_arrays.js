/**
 * Tutorial: https://youtu.be/txjmvEPlAtU?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * Arrays in JavaScript
 * ====================
 * 
 * An array is a data structure that can hold a collection of values. Arrays can contain a mix of different data types.
 * You can store strings, booleans, numbers, or even objects all in the same array. Arrays are resizable, meaning you do not
 * have to declare the size of an array before creating it. JavaScript arrays are zero-indexed, meaning the first element 
 * has an index of 0, the second element has an index of 1, and so on. The insertion order of elements is maintained.
 * 
 * Key Points:
 * -----------
 * - Arrays are resizable.
 * - Arrays can hold mixed data types (e.g., strings, booleans, numbers, objects).
 * - Arrays are zero-indexed.
 * - Arrays maintain the order of insertion.
 * - Arrays are iterables and can be used with a for...of loop.
 * - Common array methods include map, filter, reduce, concat, slice, and splice.
 * 
 * Big-O Notation of Time Complexity
 * ---------------------------------
 * Understanding the time complexity of common array operations is crucial for writing efficient code. Here are the 
 * time complexities for various operations on JavaScript arrays:
 * 
 * 1. Insert / Remove from End: O(1) - Constant time complexity
 *    - Adding or removing an element from the end of the array is very fast, as it doesn't require shifting any other elements.
 * 
 * 2. Insert / Remove from Beginning: O(n) - Linear time complexity
 *    - Adding or removing an element from the beginning of the array requires shifting all the other elements, making it slower.
 * 
 * 3. Access: O(1) - Constant time complexity
 *    - Accessing an element by its index is very fast.
 * 
 * 4. Search: O(n) - Linear time complexity
 *    - Searching for an element requires checking each element one by one in the worst case.
 * 
 * 5. Push / Pop: O(1) - Constant time complexity
 *    - Pushing (adding) or popping (removing) an element from the end of the array is very fast.
 * 
 * 6. Shift / Unshift / Concat / Slice / Splice: O(n) - Linear time complexity
 *    - Operations like shift (removing from the beginning), unshift (adding to the beginning), concat (combining arrays), 
 *      slice (extracting a section of the array), and splice (adding/removing elements at a specific index) involve 
 *      shifting elements and thus have linear time complexity.
 * 
 * 7. forEach / Map / Filter / Reduce: O(n) - Linear time complexity
 *    - Iterating over the array with methods like forEach, map, filter, and reduce involves processing each element once, 
 *      leading to linear time complexity.
 */



// Initializing an array with mixed data types
const arr = [1, 2, 3, "Shayon", 4, 5];

// Adding an element to the end of the array
// Time Complexity: O(1), Space Complexity: O(1)
arr.push(4);

// Adding an element to the beginning of the array
// Time Complexity: O(n), Space Complexity: O(1)
arr.unshift(0);

// Removing an element from the end of the array
// Time Complexity: O(1), Space Complexity: O(1)
arr.pop();

// Removing an element from the beginning of the array
// Time Complexity: O(n), Space Complexity: O(1)
arr.shift();

// Iterating over the array and printing each element
// Time Complexity: O(n), Space Complexity: O(1)
for (const a of arr) {
    console.log(a);
}

/**
 * Explanation of Time and Space Complexity:
 * 
 * - arr.push(4):
 *   Adds an element to the end of the array.
 *   - Time Complexity: O(1) because it involves adding a single element to the end without needing to shift other elements.
 *   - Space Complexity: O(1) because it requires a constant amount of additional space regardless of the size of the array.
 * 
 * - arr.unshift(0):
 *   Adds an element to the beginning of the array.
 *   - Time Complexity: O(n) because it needs to shift all existing elements one position to the right.
 *   - Space Complexity: O(1) because it requires a constant amount of additional space regardless of the size of the array.
 * 
 * - arr.pop():
 *   Removes an element from the end of the array.
 *   - Time Complexity: O(1) because it involves removing a single element from the end without needing to shift other elements.
 *   - Space Complexity: O(1) because it requires a constant amount of additional space regardless of the size of the array.
 * 
 * - arr.shift():
 *   Removes an element from the beginning of the array.
 *   - Time Complexity: O(n) because it needs to shift all existing elements one position to the left.
 *   - Space Complexity: O(1) because it requires a constant amount of additional space regardless of the size of the array.
 * 
 * - for (const a of arr):
 *   Iterates over the array and prints each element.
 *   - Time Complexity: O(n) because it involves visiting each element of the array once.
 *   - Space Complexity: O(1) because it requires a constant amount of additional space regardless of the size of the array.
 */

