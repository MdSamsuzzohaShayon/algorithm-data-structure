/**
 * 01:29:30 - https://youtu.be/oBt53YbR9Kk?t=5371
 * 
 * Problem:
 * Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.
 * The function should return an array containing any combination of elements that add up to exactly the targetSum. 
 * If there is no combination that adds up to the targetSum, then return null.
 * If there are multiple combinations possible, you may return any single one.
 */

/**
 * Naive recursive function to determine how to sum to the targetSum using numbers from the array.
 * 
 * @param {number} targetSum - The target sum to achieve.
 * @param {number[]} numbers - The array of numbers to use.
 * @returns {number[] | null} - An array of numbers that add up to targetSum or null if not possible.
 */
function howSum(targetSum, numbers) {
    if (targetSum === 0) return []; // Base case: If targetSum is 0, we've successfully generated the targetSum
    if (targetSum < 0) return null; // Base case: If targetSum is negative, it's not possible to generate the targetSum

    // Loop through each number in the array
    for (const num of numbers) {
        const remainder = targetSum - num; // Calculate the remainder after subtracting the current number
        const remainderResult = howSum(remainder, numbers); // Recursively call howSum with the remainder
        if (remainderResult !== null) {
            return [...remainderResult, num]; // If a valid combination is found, return it with the current number
        }
    }

    return null; // If no valid combination is found, return null
}
// Brute Force solution
// m = target sum
// n = numbers.length
// Time complexity: O(n^m * m) - Exponential time complexity
// Space complexity: O(m) - Linear space complexity

console.log("===== Brute Force =====");
console.log(howSum(7, [2, 3])); // Output: [3, 2, 2]
console.log(howSum(7, [5, 3, 4, 7])); // Output: [4, 3]
console.log(howSum(7, [2, 4])); // Output: null
console.log(howSum(8, [2, 3, 5])); // Output: [2, 2, 2, 2]
console.log(howSum(300, [7, 14])); // Output: null

/**
 * Optimized function to determine how to sum to the targetSum using numbers from the array using memoization.
 * 
 * Memoization stores the results of expensive function calls and returns the cached
 * result when the same inputs occur again, thus avoiding redundant calculations.
 * 
 * @param {number} targetSum - The target sum to achieve.
 * @param {number[]} numbers - The array of numbers to use.
 * @param {object} memo - An object to store previously computed results.
 * @returns {number[] | null} - An array of numbers that add up to targetSum or null if not possible.
 */
function optimizedHowSum(targetSum, numbers, memo = {}) {
    if (targetSum in memo) return memo[targetSum]; // If the result is already in the memo, return it
    if (targetSum === 0) return []; // Base case: If targetSum is 0, we've successfully generated the targetSum
    if (targetSum < 0) return null; // Base case: If targetSum is negative, it's not possible to generate the targetSum

    // Loop through each number in the array
    for (const num of numbers) {
        const remainder = targetSum - num; // Calculate the remainder after subtracting the current number
        const remainderResult = optimizedHowSum(remainder, numbers, memo); // Recursively call optimizedHowSum with the remainder
        if (remainderResult !== null) {
            memo[targetSum] = [...remainderResult, num]; // Store the result in the memo and return it with the current number
            return memo[targetSum];
        }
    }

    memo[targetSum] = null; // Store the result in the memo
    return null; // If no valid combination is found, return null
}
// Memoized solution
// m = target sum
// n = numbers.length
// Time complexity: O(n * m^2) - Polynomial time complexity
// Space complexity: O(m^2) - Polynomial space complexity

console.log("===== Memoization =====");
console.log(optimizedHowSum(7, [2, 3])); // Output: [3, 2, 2]
console.log(optimizedHowSum(7, [5, 3, 4, 7])); // Output: [4, 3]
console.log(optimizedHowSum(7, [2, 4])); // Output: null
console.log(optimizedHowSum(8, [2, 3, 5])); // Output: [2, 2, 2, 2]
console.log(optimizedHowSum(300, [7, 14])); // Output: null

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
 * Example: howSum Problem
 * 
 * The howSum problem is a classic example of a problem that can be optimized using
 * dynamic programming. The goal is to determine how to sum to a targetSum using numbers 
 * from a given array. An element of the array can be used multiple times.
 * 
 * Naive Approach:
 * The naive approach uses a simple recursive function to determine how to generate the 
 * targetSum. However, this approach is highly inefficient for large targetSum values because
 * it involves redundant calculations and has an exponential time complexity of O(n^m * m).
 * 
 * Optimized Approach:
 * Using memoization, we can optimize the calculation of the howSum problem. We store 
 * the results of subproblems in a memo object and reuse these results whenever the same 
 * subproblem occurs. This reduces the time complexity to O(n * m^2), making the function 
 * much more efficient for large targetSum values.
 */
