/**
 * 01:52:07 - https://youtu.be/oBt53YbR9Kk?t=6727
 * 
 * Problem:
 * Write a function `bestSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.
 * The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.
 * If there is a tie for the shortest combination, you may return any one of the shortest.
 */

/**
 * Naive recursive function to determine the shortest combination of numbers that sum to the targetSum.
 * 
 * @param {number} targetSum - The target sum to achieve.
 * @param {number[]} numbers - The array of numbers to use.
 * @returns {number[] | null} - An array of numbers that add up to targetSum or null if not possible.
 */
function bestSum(targetSum, numbers) {
    if (targetSum === 0) return []; // Base case: If targetSum is 0, return an empty array
    if (targetSum < 0) return null; // Base case: If targetSum is negative, return null

    let shortestCombination = null; // Variable to store the shortest combination found

    // Loop through each number in the array
    for (const num of numbers) {
        const remainder = targetSum - num; // Calculate the remainder after subtracting the current number
        const remainderCombination = bestSum(remainder, numbers); // Recursively call bestSum with the remainder
        if (remainderCombination !== null) {
            const combination = [...remainderCombination, num]; // Create a new combination including the current number
            // If the current combination is shorter than the current shortest, update the shortestCombination
            if (shortestCombination === null || combination.length < shortestCombination.length) {
                shortestCombination = combination;
            }
        }
    }
    return shortestCombination; // Return the shortest combination found
}

// Brute Force
// m = target sum
// n = numbers.length
// Time complexity: O(n^m * m) - Exponential time complexity
// Space complexity: O(m^2) - Quadratic space complexity

console.log("===== Brute Force =====");
console.log(bestSum(7, [5, 3, 4, 7])); // Output: [7]
console.log(bestSum(8, [2, 3, 5])); // Output: [3, 5]
console.log(bestSum(8, [1, 4, 5])); // Output: [4, 4]
console.log(bestSum(32, [1, 2, 5, 25])); // Output: [25, 5, 2]

// Optimized version using memoization

/**
 * Optimized function to determine the shortest combination of numbers that sum to the targetSum using memoization.
 * 
 * Memoization stores the results of expensive function calls and returns the cached
 * result when the same inputs occur again, thus avoiding redundant calculations.
 * 
 * @param {number} targetSum - The target sum to achieve.
 * @param {number[]} numbers - The array of numbers to use.
 * @param {object} memo - An object to store previously computed results.
 * @returns {number[] | null} - An array of numbers that add up to targetSum or null if not possible.
 */
function optimizedBestSum(targetSum, numbers, memo = {}) {
    if (targetSum in memo) return memo[targetSum]; // If the result is already in the memo, return it
    if (targetSum === 0) return []; // Base case: If targetSum is 0, return an empty array
    if (targetSum < 0) return null; // Base case: If targetSum is negative, return null

    let shortestCombination = null; // Variable to store the shortest combination found

    // Loop through each number in the array
    for (const num of numbers) {
        const remainder = targetSum - num; // Calculate the remainder after subtracting the current number
        const remainderCombination = optimizedBestSum(remainder, numbers, memo); // Recursively call optimizedBestSum with the remainder
        if (remainderCombination !== null) {
            const combination = [...remainderCombination, num]; // Create a new combination including the current number
            // If the current combination is shorter than the current shortest, update the shortestCombination
            if (shortestCombination === null || combination.length < shortestCombination.length) {
                shortestCombination = combination;
            }
        }
    }
    memo[targetSum] = shortestCombination; // Store the result in the memo
    return shortestCombination; // Return the shortest combination found
}

// Memoized
// m = target sum
// n = numbers.length
// Time complexity: O(n * m^2) - Polynomial time complexity
// Space complexity: O(m^2) - Quadratic space complexity

console.log("===== Memoized =====");
console.log(optimizedBestSum(7, [5, 3, 4, 7])); // Output: [7]
console.log(optimizedBestSum(8, [2, 3, 5])); // Output: [3, 5]
console.log(optimizedBestSum(8, [1, 4, 5])); // Output: [4, 4]
console.log(optimizedBestSum(32, [1, 2, 5, 25])); // Output: [25, 5, 2]


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
 * Example: bestSum Problem
 * 
 * The bestSum problem is a classic example of a problem that can be optimized using
 * dynamic programming. The goal is to determine the shortest combination of numbers 
 * that sum to a targetSum using numbers from a given array.
 * 
 * Naive Approach:
 * The naive approach uses a simple recursive function to determine the shortest combination
 * of numbers that sum to the targetSum. However, this approach is highly inefficient for 
 * large targetSum values because it involves redundant calculations and has an exponential 
 * time complexity of O(n^m * m).
 * 
 * Optimized Approach:
 * Using memoization, we can optimize the calculation of the bestSum problem. We store 
 * the results of subproblems in a memo object and reuse these results whenever the same 
 * subproblem occurs. This reduces the time complexity to O(n * m^2), making the function 
 * much more efficient for large targetSum values.
 */
