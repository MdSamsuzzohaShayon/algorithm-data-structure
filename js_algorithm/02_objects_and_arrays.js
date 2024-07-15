// https://www.youtube.com/watch?v=XkhLTlFXxbI&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=5


// ===== Object =====
const person = {
    firstName: "Bruce",
    lastName: "Wayne",
}

console.log(person.firstName); // access - O(1)
delete person.firstName; console.log(person); // Remove - O(1)
person.age = 20; console.log(person); // Insert - O(1)

// Search - O(n)
console.log(Object.keys()) // - O(n)
console.log(Object.values()) // - O(n)
console.log(Object.entries()) // - O(n)



// ===== Array =====
const odd = [1, 3, 5, 7, 9];

// Insert / remove at the end - O(1)
// Insert / remove at the beginning - O(n)
// Access - O(1)
// Search - O(n)
// Push/pop - O(n)
// Shift/unshift/concat/slice/splice - O(n)
// forEach/map/filter/reduce - O(n)
