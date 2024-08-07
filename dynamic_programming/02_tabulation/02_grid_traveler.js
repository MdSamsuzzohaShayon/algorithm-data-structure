/**
 * 03:22:10 - https://youtu.be/oBt53YbR9Kk?t=12134
 * 
 * 
 * Tabulation in Dynamic Programming:
 * - A bottom-up approach to solve problems by solving and storing solutions to all sub-problems
 * - Start with the smallest sub-problems and build up to the solution of the original problem
 * - This approach avoids the overhead of recursive calls and usually has better performance
 *
 * Problem: Grid Traveler
 * - You are a traveler on a 2D grid starting from the top-left corner
 * - Your goal is to travel to the bottom-right corner
 * - You can only move down or right
 * - Calculate the number of ways to travel to the goal on a grid with dimensions m*n
 * 
 * Time Complexity: O(mn)
 * Space Complexity: O(mn)
 *
 * Let's implement the grid traveler problem using Tabulation:
 */

function gridTraveler(m, n) {
    // Create a table with m+1 rows and n+1 columns, initially filled with 0
    const table = new Array(m + 1)
        .fill()
        .map(() => new Array(n + 1)
            .fill(0));
    
    // The starting position (1,1) has one way to be reached
    table[1][1] = 1;

    // Iterate through the table
    for (let i = 0; i <= m; i++) {
        for (let j = 0; j <= n; j++) {
            const curr = table[i][j];
            // If moving right is within bounds, add current value to the right cell
            if (j + 1 <= n) table[i][j + 1] += curr;
            // If moving down is within bounds, add current value to the bottom cell
            if (i + 1 <= m) table[i + 1][j] += curr;
        }
    }

    // Return the value at the bottom-right corner, which is the number of ways to reach the goal
    return table[m][n];
}

// Test cases to validate the implementation
console.log(gridTraveler(1, 1));  // Output: 1
console.log(gridTraveler(2, 3));  // Output: 3
console.log(gridTraveler(3, 2));  // Output: 3
console.log(gridTraveler(3, 3));  // Output: 6
console.log(gridTraveler(18, 18)); // Output: 2333606220

/**
 * Explanation of the Code:
 * 1. We initialize a table with m+1 rows and n+1 columns, all set to 0.
 * 2. We set the starting position (1,1) in the table to 1, as there's one way to be at the start.
 * 3. We iterate through the table using nested loops for rows and columns.
 * 4. For each cell, we add the current value to the right and bottom cells, if they are within bounds.
 * 5. Finally, we return the value at the bottom-right corner of the table, which is the number of ways to travel to the goal.
 *
 * Related Subtopics:
 * - Memoization: Another dynamic programming approach using a top-down method with caching
 * - Space Optimization: Techniques to reduce space complexity in dynamic programming
 * - Common DP Problems: Coin change, longest common subsequence, knapsack problem, etc.
 */
