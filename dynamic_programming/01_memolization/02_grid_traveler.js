/**
 * Grid Traveler - Memoization
 * 00:38:40 - https://youtu.be/oBt53YbR9Kk?t=2321
 * 
 * 
 * Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. 
 * You may only move down or right. In how many ways can you travel to the goal on a grid with dimensions m*n?
 * 
 * Write a function `gridTraveler(m,n)` that calculates this.
 */

/**
 * Naive recursive function to calculate the number of ways to travel on an m*n grid.
 * 
 * @param {number} m - The number of rows in the grid.
 * @param {number} n - The number of columns in the grid.
 * @returns {number} - The number of ways to travel to the bottom-right corner.
 */
function gridTraveler(m, n) {
    // Base case: 1x1 grid has only 1 way to travel (stay in place)
    if (m === 1 && n === 1) return 1;
    // Base case: Grid with zero rows or columns has no way to travel
    if (m === 0 || n === 0) return 0;
    // Recursive case: Sum of ways to travel from the cell above and the cell to the left
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1);
}
// Brute force solution
// Time complexity: O(2^(m+n)) - Exponential time complexity
// Space complexity: O(m+n) - Linear space complexity

// Example usage of the naive grid traveler function
console.log(gridTraveler(1, 1)); // Output: 1
console.log(gridTraveler(2, 3)); // Output: 3
console.log(gridTraveler(3, 2)); // Output: 3
console.log(gridTraveler(3, 3)); // Output: 6
console.log(gridTraveler(16, 16)); // Output: 155117520 (This will take a long time)

/**
 * Optimized function to calculate the number of ways to travel on an m*n grid using memoization.
 * 
 * Memoization stores the results of expensive function calls and returns the cached
 * result when the same inputs occur again, thus avoiding redundant calculations.
 * 
 * @param {number} m - The number of rows in the grid.
 * @param {number} n - The number of columns in the grid.
 * @param {object} memo - An object to store previously computed results.
 * @returns {number} - The number of ways to travel to the bottom-right corner.
 */
function optimizedGridTraveler(m, n, memo = {}) {
    // Create a unique key for the memo object based on the grid dimensions
    const key = `${m},${n}`;
    // If the result for the current grid dimensions is already in the memo, return it
    if (key in memo) return memo[key];
    // Base case: 1x1 grid has only 1 way to travel (stay in place)
    if (m === 1 && n === 1) return 1;
    // Base case: Grid with zero rows or columns has no way to travel
    if (m === 0 || n === 0) return 0;
    // Recursive case: Sum of ways to travel from the cell above and the cell to the left
    memo[key] = optimizedGridTraveler(m - 1, n, memo) + optimizedGridTraveler(m, n - 1, memo);
    return memo[key]; // Return the computed result
}
// Optimized solution with memoization
// Time complexity: O(m*n) - Polynomial time complexity
// Space complexity: O(m+n) - Linear space complexity

// Example usage of the optimized grid traveler function
console.log(optimizedGridTraveler(1, 1)); // Output: 1
console.log(optimizedGridTraveler(2, 3)); // Output: 3
console.log(optimizedGridTraveler(3, 2)); // Output: 3
console.log(optimizedGridTraveler(3, 3)); // Output: 6
console.log(optimizedGridTraveler(16, 16)); // Output: 155117520

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
 * Example: Grid Traveler
 * 
 * The grid traveler problem is a classic example of a problem that can be optimized using
 * dynamic programming. The goal is to find the number of ways to travel from the top-left 
 * corner to the bottom-right corner of a grid with dimensions m*n, moving only down or right.
 * 
 * Naive Approach:
 * The naive approach uses a simple recursive function to calculate the number of ways to 
 * travel on an m*n grid. However, this approach is highly inefficient for large grid 
 * dimensions because it involves redundant calculations and has an exponential time 
 * complexity of O(2^(m+n)).
 * 
 * Optimized Approach:
 * Using memoization, we can optimize the calculation of the grid traveler problem. We store 
 * the results of subproblems in a memo object and reuse these results whenever the same 
 * subproblem occurs. This reduces the time complexity to O(m*n), making the function much 
 * more efficient for large grid dimensions.
 */
