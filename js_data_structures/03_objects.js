/**
 * Tutorial: https://youtu.be/1c9CArj66mU?list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP
 * 
 * An object is an unordered collection of key-value pairs. The key must either be a string or symbol data type where as the value can be of any data type.
 * To retrieve a value, you can use the corresponding key. This can be achieved using the dot notation or bracket notation.
 * An object is not an iterable. You can not use it with a for of loop.
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

/**
 * Big-O notation of time complexity of Object
 * insert - O(1) Constant time
 * Remove - O(1) Constant time
 * Access - O(1) Constant time
 * Search - O(n) Linear time
 * Object.keys() - O(n) Linear time
 * Object.values() - O(n) Linear time
 * Object.entries() - O(n) Linear time
 */