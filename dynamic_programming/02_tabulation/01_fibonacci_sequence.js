/**
 * YouTube Tutorial: https://youtu.be/oBt53YbR9Kk?t=11452
 * 
 * 
 * Tabulation in Dynamic Programming:
 * - A bottom-up approach to solve problems by solving and storing solutions to all sub-problems
 * - Start with the smallest sub-problems and build up to the solution of the original problem
 * - This approach avoids the overhead of recursive calls and usually has better performance
 *
 * Key Concepts:
 * 1. Bottom-Up Approach: Solve sub-problems starting from the smallest
 * 2. Table: Use an array (table) to store the solutions to sub-problems
 * 3. Iterative: Use loops instead of recursion
 * 4. Space Complexity: Requires additional space to store the table
 * 5. Time Complexity: Generally efficient as it avoids redundant calculations
 *
 * Example: Fibonacci Sequence
 * - Problem: Compute the n-th Fibonacci number
 * - Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
 * - The 0th number is 0 and the 1st number is 1
 * - Each subsequent number is the sum of the previous two numbers
 *
 * Let's implement the Fibonacci sequence using Tabulation:
 */

function fibonacciSequence(n) {
    // Create a table with n+1 elements, initially filled with 0
    const table = new Array(n + 1).fill(0);

    // The 1st Fibonacci number is 1
    table[1] = 1;

    // Iterate through the table
    for (let i = 0; i <= n; i++) {
        // Ensure we don't go out of bounds
        if (i + 1 <= n) {
            // Add the current value to the next position
            table[i + 1] += table[i];
        }
        if (i + 2 <= n) {
            // Add the current value to the position after the next
            table[i + 2] += table[i];
        }
    }

    // Return the n-th Fibonacci number
    return table[n];
}

// Test cases to validate the implementation
console.log(fibonacciSequence(6));  // Output: 8
console.log(fibonacciSequence(7));  // Output: 13
console.log(fibonacciSequence(8));  // Output: 21
console.log(fibonacciSequence(50)); // Output: 12586269025

/**
 * Explanation of the Code:
 * 1. We initialize a table with n+1 elements, all set to 0.
 * 2. We set the 1st Fibonacci number in the table to 1.
 * 3. We iterate through the table from 0 to n.
 * 4. For each index, we add the current value to the next and the position after the next,
 *    ensuring we don't go out of bounds.
 * 5. Finally, we return the value at index n, which is the n-th Fibonacci number.
 *
 * Related Subtopics:
 * - Memoization: Another dynamic programming approach using a top-down method with caching
 * - Space Optimization: Techniques to reduce space complexity in dynamic programming
 * - Common DP Problems: Coin change, longest common subsequence, knapsack problem, etc.
 */
