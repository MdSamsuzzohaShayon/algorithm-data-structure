// Tutorial - https://www.youtube.com/watch?v=tQjd29Rmo_A&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=7

/*
 * Problem - Given a number 'n', find the first 'n' elements of the Fibonacci sequence
 * In mathematic, the Fibonacci sequence is a sequence in which each number is the sum of two preceding ones.
 * The first two numbers in the sequence are 0 and 1
 * Example 1: fibonacci(2)=[0,1]
 * Example 2: fibonacci(3)=[0,1,1] this is because the third number (1) is sum of previous two numbers (0+1)
 * Example 3: fibonacci(7)=[0, 1, 1, 2, 3, 5, 8]
 */

function fibonacci(n){
  const fib = [0, 1];
  for (let i = 2; i < n; i++) {
    fib[i] = fib[i-1] + fib[i-2]; // As value o n increases this line execution increases therefore, this is linear time complexity
  }
  return fib;
}

console.log(fibonacci(2)); // Expected return: [0, 1]
console.log(fibonacci(3)); // Expected return: [0, 1, 1]
console.log(fibonacci(7)); // Expected return: [0, 1, 1, 2, 3, 5, 8]

/*
 * Big O Guide
 * ====================================
 * Loop - O(n)
 * Nested Loop - O(n^2)
 * Input size reduced by half - O(log n)
 */
