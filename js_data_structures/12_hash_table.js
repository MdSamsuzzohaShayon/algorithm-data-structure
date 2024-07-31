/**
 * Tutorial-1: https://www.youtube.com/watch?v=-Df9ipREbuM&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=62
 * Tutorial-2: https://www.youtube.com/watch?v=y3CcHKEM8r8&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=63
 * Tutorial-3: https://www.youtube.com/watch?v=kTh5nAqCkOA&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=65
 * 
 * Hash Table
 * ----------
 * A hash table, also known as a hash map, is a data structure used to store key-value pairs.
 * Given a key, you can associate a value with that key for very fast lookup.
 * 
 * JavaScript's Object is a special implementation of the hash table data structure.
 * However, the Object class adds its own keys. Keys that you input may conflict and overwrite the inherited default properties.
 * 
 * In a hash table:
 * - We store the key-value pairs in a fixed-sized array.
 * - Arrays have a numeric index.
 * 
 * The key challenge is:
 * How do we go from using a string as an index to using a number as an index?
 * 
 * Solution:
 * - A hashing function accepts the string key, converts it into a hash code using a defined logic, 
 *   and then maps it to a numeric index that is within the bounds of the array.
 * - Using this index, we store the value.
 * - The same hashing function is reused to retrieve the value given a key.
 * 
 * ES6 Maps:
 * - Maps, introduced in 2015, also allow you to store key-value pairs.
 * 
 * Primary Functions of Hash Table:
 * - `set(key, value)`: Store a key-value pair.
 * - `get(key)`: Retrieve a value given its key.
 * - `remove(key)`: Delete a key-value pair.
 * 
 * Usage of Hash Tables:
 * ---------------------
 * Hash tables are typically implemented where constant time lookup and insertion are required. 
 * Examples include:
 * - Database indexing: Quickly accessing records.
 * - Caches: Fast data retrieval.
 * - Symbol tables in interpreters and compilers: Storing variable names.
 * - Routing tables in networking: Determining the next hop for data packets.
 * - Associative arrays: Arrays that use non-numeric keys.
 */


/**
 * HashTable Class
 * ---------------
 * This class represents a simple implementation of a hash table, a data structure that stores key-value pairs for efficient retrieval.
 * It uses a fixed-size array to store the values and a hashing function to map string keys to numeric indices.
 */

class HashTable {
    constructor(size) {
        // Initialize the table with the given size
        this.table = new Array(size);
        this.size = size;
    }

    /**
     * Hashing Function
     * ----------------
     * The hash function converts a string key into a numeric index.
     * The key is transformed into a hash code by summing the character codes of its characters.
     * The modulus operator ensures the index is within the bounds of the array.
     * 
     * @param {string} key - The key to be hashed.
     * @returns {number} - The numeric index corresponding to the key.
     */
    hash(key) {
        let total = 0;
        // Iterate over each character in the key
        for (let i = 0; i < key.length; i++) {
            // Add the character code of each character to the total
            // charCodeAt method returns an integer between 0 and 65535 representing the UTF-16 code unit at the given index.
            const char_code = key.charCodeAt(i); // Get the Unicode of the first character in a string
            total += char_code;
        }
        // Return the index within the bounds of the array
        return total % this.size;
    }

    /**
     * Set Function
     * ------------
     * Stores a key-value pair in the hash table.
     * The key is hashed to find the appropriate index, and the value is stored at that index.
     * 
     * @param {string} key - The key associated with the value.
     * @param {*} value - The value to be stored.
     */
    set(key, value) {
        // Hash the key to get the index where the value should be stored.
        const index = this.hash(key);

        // Retrieve the bucket (linked list) at the hashed index.
        const bucket = this.table[index];

        // If there is no bucket at this index, create a new bucket (array of key-value pairs).
        if (!bucket) {
            this.table[index] = [[key, value]];
        } else {
            // If a bucket exists, find the item with the same key.
            const sameKeyItem = bucket.find(item => item[0] === key);

            if (sameKeyItem) {
                // If an item with the same key is found, update its value.
                sameKeyItem[1] = value;
            } else {
                // If no item with the same key is found, add a new key-value pair to the bucket.
                bucket.push([key, value]);
            }
        }
    }


    /**
     * Get Function
     * ------------
     * Retrieves the value associated with a given key.
     * The key is hashed to find the index, and the value at that index is returned.
     * 
     * @param {string} key - The key whose value is to be retrieved.
     * @returns {*} - The value associated with the key, or undefined if not found.
     */
    get(key) {
        const index = this.hash(key);
        // return this.table[index];
        const bucket = this.table[index];
        if (bucket) {
            const sameKeyItem = bucket.find(item => item[0] === key);
            if (sameKeyItem) {
                return sameKeyItem[1];
            }
        }
        return undefined;
    }

    /**
     * Remove Function
     * ---------------
     * Deletes a key-value pair from the hash table.
     * The key is hashed to find the index, and the value at that index is set to undefined.
     * 
     * @param {string} key - The key to be removed.
     */
    remove(key) {
        const index = this.hash(key);
        // this.table[index] = undefined;
        const bucket = this.table[index];
        if(bucket){
            const sameKeyItem = bucket.find(item=> item[0] === key);
            if(sameKeyItem) bucket.splice(bucket.indexOf(sameKeyItem), 1);
        }
    }

    /**
     * Display Function
     * ----------------
     * Displays the contents of the hash table.
     * It iterates through the table and logs the index and value of non-empty slots.
     */
    display() {
        for (let i = 0; i < this.table.length; i++) {
            if (this.table[i]) {
                console.log(i, this.table[i]);
            }
        }
    }
}

// Example usage
const table = new HashTable(50);
table.set("name", "Neymar JR");
table.set("age", 30);
table.display();
console.log(table.get("name"));
// table.remove("name");
table.set("name", "Hulk"); // Overwrite
table.set("mane", "The Increadiable"); // mane and same will have same value when hash their string unicode
table.display();
table.remove("mane");
table.display();

// Average time complexity is O(1)