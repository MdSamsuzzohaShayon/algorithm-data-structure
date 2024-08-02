/**
 * 00:02:43 - https://youtu.be/oBt53YbR9Kk?t=223
 * 
 * Dynamic Programming with Fibonacci Sequence
 * 
 * This script demonstrates the use of dynamic programming to optimize the calculation
 * of Fibonacci numbers. It includes both a naive recursive implementation and an 
 * optimized version using memoization.
 */

/**
 * Adds commas to a large integer for better readability.
 * 
 * @param {number} number - The large integer to format.
 * @returns {string} - The formatted number with commas.
 */
function addCommas(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

/**
 * Naive recursive function to calculate the n-th Fibonacci number.
 * 
 * @param {number} n - The position in the Fibonacci sequence.
 * @returns {number} - The n-th Fibonacci number.
 */
const fib = (n) => {
    if (n <= 2) return 1; // Base case: the 1st and 2nd Fibonacci numbers are 1
    return fib(n - 1) + fib(n - 2); // Recursive case: sum of the two preceding numbers
};

// Example usage of the naive Fibonacci function
console.log(fib(4)); // Output: 3
console.log(fib(5)); // Output: 5
console.log(fib(10)); // Output: 55

console.log("==========Before Optimization==========");
let dateTime = new Date();
console.log(`Start ${dateTime.getMinutes()} minutes and ${dateTime.getSeconds()} seconds `);
console.log(fib(45)); // This lacks efficiency and takes a long time for large inputs
dateTime = new Date();
console.log(`End ${dateTime.getMinutes()} minutes and ${dateTime.getSeconds()} seconds `);

/**
 * Optimized function to calculate the n-th Fibonacci number using memoization.
 * 
 * Memoization stores the results of expensive function calls and returns the cached
 * result when the same inputs occur again, thus avoiding redundant calculations.
 * 
 * @param {number} n - The position in the Fibonacci sequence.
 * @param {object} memo - An object to store previously computed Fibonacci numbers.
 * @returns {number} - The n-th Fibonacci number.
 */
const optimizedFib = (n, memo = {}) => {
    if (n in memo) return memo[n]; // Check if result is already in the memo object
    if (n <= 2) return 1; // Base case: the 1st and 2nd Fibonacci numbers are 1
    memo[n] = optimizedFib(n - 1, memo) + optimizedFib(n - 2, memo); // Store result in memo
    return memo[n]; // Return the computed Fibonacci number
};

console.log("==========After Optimization==========");
dateTime = new Date();
console.log(`Start ${dateTime.getMinutes()} minutes and ${dateTime.getSeconds()} seconds `);
console.log(optimizedFib(45)); // Much more efficient than the naive approach
dateTime = new Date();
console.log(`End ${dateTime.getMinutes()} minutes and ${dateTime.getSeconds()} seconds `);

/**
 * Detailed Document: Dynamic Programming with JavaScript
 * 
 * Dynamic Programming (DP) is a method for solving complex problems by breaking them down
 * into simpler subproblems. It is applicable when the problem can be divided into 
 * overlapping subproblems with optimal substructure (i.e., the optimal solution to the 
 * problem can be constructed from the optimal solutions of its subproblems).
 * 
 * There are two main approaches to dynamic programming:
 * 1. Top-down approach (Memoization): This approach involves solving the problem recursively
 *    and storing the results of subproblems to avoid redundant calculations. It is 
 *    implemented using recursion and a memoization table (usually a dictionary or array).
 * 
 * 2. Bottom-up approach (Tabulation): This approach involves solving the problem 
 *    iteratively, starting from the smallest subproblems and building up to the final 
 *    solution. It is implemented using loops and a table to store the results of subproblems.
 * 
 * Example: Fibonacci Sequence
 * 
 * The Fibonacci sequence is a classic example of a problem that can be optimized using
 * dynamic programming. The n-th Fibonacci number is defined as the sum of the (n-1)-th 
 * and (n-2)-th Fibonacci numbers, with the 1st and 2nd Fibonacci numbers being 1.
 * 
 * Naive Approach:
 * The naive approach uses a simple recursive function to calculate the n-th Fibonacci number.
 * However, this approach is highly inefficient for large values of n because it involves 
 * redundant calculations and has an exponential time complexity of O(2^n).
 * 
 * Optimized Approach:
 * Using memoization, we can optimize the calculation of the Fibonacci sequence. We store 
 * the results of subproblems in a memo object and reuse these results whenever the same 
 * subproblem occurs. This reduces the time complexity to O(n), making the function much 
 * more efficient for large values of n.
 */
