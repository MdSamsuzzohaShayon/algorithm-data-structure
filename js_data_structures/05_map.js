/**
 * Tutorial: https://youtu.be/XOpKmpRh69Y?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * 
 * Map in JavaScript
 * =================
 * A Map is an ordered collection of key-value pairs where both keys and values can be of any data type.
 * 
 * Basic Operations
 * ----------------
 * 1. Creating a Map:
 *    let map = new Map();
 * 
 * 2. Setting values:
 *    map.set('key', 'value'); // Adds a key-value pair to the map
 *    map.set(1, 'one');       // Keys can be of any type
 * 
 * 3. Retrieving values:
 *    map.get('key'); // Returns the value associated with 'key'
 * 
 * 4. Checking for a key:
 *    map.has('key'); // Returns true if 'key' is in the map
 * 
 * 5. Deleting a key:
 *    map.delete('key'); // Removes the key-value pair with 'key'
 * 
 * 6. Getting the size of the map:
 *    map.size; // Returns the number of key-value pairs in the map
 * 
 * 7. Iterating over a map:
 *    for (let [key, value] of map) {
 *        console.log(key, value);
 *    }
 *    // Maps are iterables and can be used with a for-of loop
 * 
 * Maps vs Objects
 * ---------------
 * 1. Order:
 *    - Objects are unordered collections of key-value pairs.
 *    - Maps maintain the order of key-value pairs as per insertion.
 * 
 * 2. Key Types:
 *    - In Objects, keys can only be strings or symbols.
 *    - In Maps, keys can be of any type (e.g., objects, functions, primitives).
 * 
 * 3. Prototypes and Default Keys:
 *    - Objects have a prototype, which may contain default keys that can conflict with your own keys.
 *    - Maps do not have prototypes, thus avoiding potential key collisions.
 * 
 * 4. Size:
 *    - The number of items in an Object must be determined manually (e.g., using Object.keys(obj).length).
 *    - The number of items in a Map is readily available through the `size` property.
 * 
 * 5. Functionality:
 *    - Objects can store data and have methods (functions) attached to them.
 *    - Maps are designed solely for storing data without any attached methods.
 * 
 * Examples
 * --------
 * Example of Map Operations:
 * 
 * let map = new Map();
 * map.set('name', 'Alice');
 * map.set('age', 30);
 * 
 * console.log(map.get('name')); // Output: Alice
 * console.log(map.size); // Output: 2
 * 
 * map.delete('age');
 * console.log(map.size); // Output: 1
 * 
 * for (let [key, value] of map) {
 *     console.log(key, value);
 * }
 * // Output:
 * // 'name' 'Alice'
 * 
 * Example of Object Operations:
 * 
 * let obj = {
 *     name: 'Bob',
 *     age: 25
 * };
 * 
 * console.log(obj.name); // Output: Bob
 * console.log(Object.keys(obj).length); // Output: 2
 * 
 * delete obj.age;
 * console.log(Object.keys(obj).length); // Output: 1
 * 
 * for (let key in obj) {
 *     if (obj.hasOwnProperty(key)) {
 *         console.log(key, obj[key]);
 *     }
 * }
 * // Output:
 * // 'name' 'Bob'
 */



// Initializing a Map with initial key-value pairs
const m = new Map([['a', 1], ['b', 2]]);

// Adding a new key-value pair to the Map
// Time Complexity: O(1), Space Complexity: O(1)
m.set('c', 3);

// Checking if a key exists in the Map
// Time Complexity: O(1), Space Complexity: O(1)
console.log(m.has("c")); // true

// Iterating over the Map and printing each key-value pair
// Time Complexity: O(n), Space Complexity: O(1)
for (const [k, v] of m) {
    console.log(`Key: ${k}, Value: ${v}`);
}

// Getting the size of the Map
// Time Complexity: O(1), Space Complexity: O(1)
console.log(m.size); // 3

// Clearing all elements from the Map
// Time Complexity: O(n), Space Complexity: O(1)
m.clear();
console.log({ m }); // Map(0) {}



