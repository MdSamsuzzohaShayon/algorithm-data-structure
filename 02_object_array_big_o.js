// https://www.youtube.com/watch?v=XkhLTlFXxbI&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=5

/*
 * An object is a collection of key value pairs
 * To insert O(1), access O(1)m, and remove O(1) a property the time complexity will be constant
 * No matter how many properties exist in a object it take same amount of time to insert of remove a property
 * To search for a value in a object the time complexity is linear
 * Object.keys() - O(1) Returns an array of all the keys
 * Object.values() - O(1) Returns an array of all the values
 * Object.entries() - O(1) Returns an array of all the key and value
 */
const personal = {
  fn : "Md",
  fn : "Shayon",
};


/*
 * Arrays are ordered - we start at index 0 and increment by 1
 * If we insert of remove an element from the end of the array the time complexity is constant
 * If we insert of remove an element from the beginning of the array the time complexity is linear because the index has to be reset for every remaining element
 * O(1) - Accessing an element is constant time complexity as fetching the first element is not different from fetching a element at position of 10000
 * O(n) - Searching for an element is still linear time complexity as the element can be the last one in the array
 * O(1) - Push and pop are constant
 * O(n) - Shift, unshift, concat, slice, splice are linear
 * For each map filter, or reduce are also linear
 */
const odd = [1, 3, 5, 7, 9];
