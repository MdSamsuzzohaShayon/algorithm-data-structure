/**
 * Tutorial: https://youtu.be/txjmvEPlAtU?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * An array is a data structure that can hold a collection of values. Arrays can contain a mix of diffrent data types. You can store strings, booleans, numbers
 * or even objects all in the same array. Arrays are resizeable. You no not have to declare the size of an array before creating it. 
 * JavaScript arrays are zero-indexed and the insertion order is maintained/ Arrays are iterables. They can be used with a for of loop.
 */


const arr = [1, 2, 3, "Shayon", 4, 5];


arr.push(4); // add element
arr.unshift(0); // add element at the beginning
arr.pop(); // remove element from the end of the array
arr.shift(); // Remove from the beginning

for (const a of arr) {
    console.log(a);
}

/// map, filter, reduce, concat, slice and, splice

// Big-O notation of time complexity 
/**
 * Insert / remove from end - O(1) Constant time complexity
 * Insert / remove from the beginning - O(n) Linear time complexity
 * Access - O(1) Constant time complexity
 * Search - O(n) Linear time complexity
 * Push / Pop - O(1) Linear time complexity
 * Shift / unshift / concat / slice / splice - O(n) Linear time complexity
 * forEach / map / filter / reduce - O(n) Linear time complexity
 */