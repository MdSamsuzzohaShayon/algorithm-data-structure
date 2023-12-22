// YouTube - https://www.youtube.com/watch?v=SZRG1bmDlx8&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=10

/*
 * Problem - Given a positive integer 'n', determine if the number is power of two or not
 * In integer is a power of two if there exists an integer 'x' such that 'n' === 2x
 * Example 1: isPowerOfTwo(1) = true (2^0)
 * Example 2: isPowerOfTwo(2) = true (2^1)
 * Example 3: isPowerOfTwo(5) = false
 */


 /*
  * Pseudocode
  * Let's say n = 8, and devide n by two repetedly until we get 1 as a result
  * 8/2 = 4 (remainder 0)
  * 4/2 = 2 (remainder 0)
  * 2/2 = 1 (remainder 0)
  * if remainder is not 0 in any step, 'n' is not a power of two
  * if remainder is 0 and 'n' comes down to 1 eventually, n is a power of two
  */


function isPowerOfTwo(n){
  if(n < 1) return false;
  while(n > 1){
    if (n%2 !== 0) return false;
    n = n / 2; // In each iteration we are reducing the value of n by half
  }
  return true;
}

console.log(isPowerOfTwo(1)); // true
console.log(isPowerOfTwo(2)); // true
console.log(isPowerOfTwo(5)); // false

/*
 * Big-O = O(log n)
 * Number of instruction execution increases as it grows but not by the same amount
 */


function isPowerOfTwobitWise(n){
  if(n<1) return false;

  console.log({n: n, '(n-1)': n-1, '(n & (n-1))': (n & (n-1))});
  // The expression (n & (n-1)) checks if the result of a bitwise AND operation between n and n-1 is equal to 0.
  /*
   * When n is a power of two (e.g., 2, 4, 8, 16, etc.), its binary representation has only one '1' bit, and the rest are '0' bits.
   * For example:
   * Binary representation of 2: 10
   * Binary representation of 4: 100
   * Binary representation of 8: 1000
   *
   * let's consider what happens when you subtract 1 from a power of two:
   * For 2: 2 - 1 = 1, and in binary, it's 1.
   * For 4: 4 - 1 = 3, and in binary, it's 11.
   * For 8: 8 - 1 = 7, and in binary, it's 111.
   * When you perform a bitwise AND operation between n and n-1, you are effectively comparing the binary representations of these two numbers.
   *
   * For a power of two, the binary representation has a single '1' bit followed by '0' bits. The binary representation of n-1 for a power of two has all '1' bits to the right of the first '1' bit. When you perform a bitwise AND operation between them, you get all '0' bits, except for the first '1' bit.
   * For 2: 10 & 01 = 00 (equal to 0)
   * For 4: 100 & 011 = 000 (equal to 0)
   * For 8: 1000 & 0111 = 0000 (equal to 0)
   */
  return (n & (n-1)) === 0;
}

console.log(isPowerOfTwobitWise(1));
console.log(isPowerOfTwobitWise(2));
console.log(isPowerOfTwobitWise(5));
/*
 * Big-O = O(1) constant
 * Number of instruction execution increases as it grows but not by the same amount
 */
