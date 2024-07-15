// https://youtu.be/SZRG1bmDlx8?list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa

function isPowerOfTwo(n) {
    if (n < 1) return false;


    while (n > 1) {
        if (n % 2 !== 0) return false;
        n = n / 2;
    }


    return true;
}

console.log(isPowerOfTwo(1));
console.log(isPowerOfTwo(2));
console.log(isPowerOfTwo(5));

// Big-O = O(log n) 


// ===== Optimal Solution =====
function isPowerOfTwoBitwise(n) {
    // Check if the number is less than 1
    if (n < 1) return false;  // If n is less than 1, it's not a power of two, return false.

    // Use bitwise AND operation to determine if n is a power of two
    // (n & (n - 1)) === 0 will be true if n is a power of two
    return (n & (n - 1)) === 0;
}

// Explanation:
// - A number is a power of two if it can be written as 2^k, where k is a non-negative integer.
// - In binary representation, a power of two has exactly one '1' bit and all other bits are '0'.
// - For example: 1 (2^0) is 0001, 2 (2^1) is 0010, 4 (2^2) is 0100, etc.
// - If n is a power of two, n - 1 will have all bits after the single '1' bit set to '1'.
// - For example: if n is 4 (0100), n - 1 is 3 (0011).
// - Applying the bitwise AND operation between n and n - 1 will result in 0 if n is a power of two,
//   because there will be no common '1' bits.

console.log("Optimal Solution =================================================");
console.log(isPowerOfTwoBitwise(1)); // true, because 1 is 2^0
console.log(isPowerOfTwoBitwise(2)); // true, because 2 is 2^1
console.log(isPowerOfTwoBitwise(5)); // false, because 5 is not a power of two

// Big-O = O(1)
// The time complexity is O(1) because the bitwise operation and comparison take constant time.
