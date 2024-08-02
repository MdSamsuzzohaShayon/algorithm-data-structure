/**
 * 01:04:52 - https://youtu.be/oBt53YbR9Kk?t=3895
 * 
 * Memoization recipe
 *      1. Make it work
 *          - Visualize the problem as a tree
 *          - Implement the tree using recursion
 *          - Test it
 *      2. Make it efficient
 *          - Add a memo object
 *          - Add a base case to return memo values
 *          - Store return values into the memo
 * 
 * Problem:
 * Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.
 * The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.
 * You may use an element of the array as many times as needed.
 * You may assume that all input numbers are non-negative.
 * 
 * Example 1:
 *      Input: canSum(7, [5, 3, 4, 7])
 *      Output: true 
 *      (it is possible to generate 7 by adding 3 + 4. Moreover, we can take 7 itself because 7 is a member of the array)
 */

/**
 * Naive recursive function to determine if targetSum can be generated using numbers from the array.
 * 
 * @param {number} targetSum - The target sum to achieve.
 * @param {number[]} numbers - The array of numbers to use.
 * @returns {boolean} - True if targetSum can be generated, otherwise false.
 */
function canSum(targetSum, numbers) {
    if (targetSum === 0) return true; // Base case: If targetSum is 0, we've successfully generated the targetSum
    if (targetSum < 0) return false;  // Base case: If targetSum is negative, it's not possible to generate the targetSum

    // Loop through each number in the array
    for (const num of numbers) {
        const remainder = targetSum - num; // Calculate the remainder after subtracting the current number
        // Recursively call canSum with the remainder and check if we can generate the remainder
        if (canSum(remainder, numbers) === true) return true;
    }

    return false; // If none of the recursive calls return true, return false
}
// Brute Force solution
// n = array length and m = target sum
// Time complexity: O(n^m) - Exponential time complexity
// Space complexity: O(m) - Linear space complexity

console.log("===== Brute Force =====");
console.log(canSum(7, [2, 3])); // Output: true
console.log(canSum(7, [5, 3, 4, 7])); // Output: true
console.log(canSum(7, [2, 4])); // Output: false
console.log(canSum(8, [2, 3, 5])); // Output: true
console.log(canSum(300, [7, 14])); // Output: false (This will take a long time)

/**
 * Optimized function to determine if targetSum can be generated using numbers from the array using memoization.
 * 
 * Memoization stores the results of expensive function calls and returns the cached
 * result when the same inputs occur again, thus avoiding redundant calculations.
 * 
 * @param {number} targetSum - The target sum to achieve.
 * @param {number[]} numbers - The array of numbers to use.
 * @param {object} memo - An object to store previously computed results.
 * @returns {boolean} - True if targetSum can be generated, otherwise false.
 */
function optimizedCanSum(targetSum, numbers, memo = {}) {
    if (targetSum in memo) return memo[targetSum]; // If the result is already in the memo, return it
    if (targetSum === 0) return true; // Base case: If targetSum is 0, we've successfully generated the targetSum
    if (targetSum < 0) return false;  // Base case: If targetSum is negative, it's not possible to generate the targetSum

    // Loop through each number in the array
    for (const num of numbers) {
        const remainder = targetSum - num; // Calculate the remainder after subtracting the current number
        // Recursively call optimizedCanSum with the remainder and check if we can generate the remainder
        if (optimizedCanSum(remainder, numbers, memo) === true) {
            memo[targetSum] = true; // Store the result in the memo
            return true;
        }
    }

    memo[targetSum] = false; // Store the result in the memo
    return false; // If none of the recursive calls return true, return false
}
// Memoized solution
// n = array length and m = target sum
// Time complexity: O(n*m) - Polynomial time complexity
// Space complexity: O(m) - Linear space complexity

console.log("===== Memoization =====");
console.log(optimizedCanSum(7, [2, 3])); // Output: true
console.log(optimizedCanSum(7, [5, 3, 4, 7])); // Output: true
console.log(optimizedCanSum(7, [2, 4])); // Output: false
console.log(optimizedCanSum(8, [2, 3, 5])); // Output: true
console.log(optimizedCanSum(300, [7, 14])); // Output: false (This will run efficiently)

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
 * Example: canSum Problem
 * 
 * The canSum problem is a classic example of a problem that can be optimized using
 * dynamic programming. The goal is to determine if it is possible to generate a targetSum
 * using numbers from a given array. An element of the array can be used multiple times.
 * 
 * Naive Approach:
 * The naive approach uses a simple recursive function to determine if the targetSum can be 
 * generated. However, this approach is highly inefficient for large targetSum values because
 * it involves redundant calculations and has an exponential time complexity of O(n^m).
 * 
 * Optimized Approach:
 * Using memoization, we can optimize the calculation of the canSum problem. We store 
 * the results of subproblems in a memo object and reuse these results whenever the same 
 * subproblem occurs. This reduces the time complexity to O(n*m), making the function much 
 * more efficient for large targetSum values.
 */
