/**
 * 04:07:23 - https://youtu.be/oBt53YbR9Kk?t=14843
 * 
 * 
 * Tabulation in Dynamic Programming:
 * - A bottom-up approach to solve problems by solving and storing solutions to all sub-problems
 * - Start with the smallest sub-problems and build up to the solution of the original problem
 * - This approach avoids the overhead of recursive calls and usually has better performance
 *
 * Problem: Best Sum
 * - Given a targetSum and an array of numbers
 * - Determine the shortest combination of numbers that add up to exactly the targetSum
 * - If there are multiple shortest combinations, return any one of them
 * 
 * Time Complexity: O(m^2 * n)
 * - m = targetSum
 * - n = length of the numbers array
 * - The outer loop runs `m` times, and for each iteration, we loop through `n` numbers.
 * - Inside the inner loop, the array operations (like checking length) can be considered O(m).
 * - Thus, the total time complexity is O(m^2 * n).
 *
 * Space Complexity: O(m^2)
 * - The table array stores at most `m` arrays, each array can have up to `m` elements in the worst case.
 * - Therefore, the space complexity is O(m^2).
 *
 * Let's implement the best sum problem using Tabulation:
 */

function bestSum(targetSum, numbers) {
    // Create a table with targetSum+1 elements, initially filled with null
    const table = new Array(targetSum + 1).fill(null);
    
    // There is exactly one way to reach a targetSum of 0: using no numbers
    table[0] = [];

    // Iterate through each index of the table from 0 to targetSum
    for (let i = 0; i <= targetSum; i++) {
        // If the current index has a valid combination
        if (table[i] !== null) {
            // Iterate through each number in the array
            for (const num of numbers) {
                // Create a new combination by adding the current number
                const combination = [...table[i], num];
                
                // If this combination is shorter than the previously stored combination
                // or if the targetSum at index i + num is not yet filled
                if (!table[i + num] || table[i + num].length > combination.length) {
                    table[i + num] = combination;
                }
            }
        }
    }

    // Return the shortest combination that adds up to targetSum, or null if no valid combination is found
    return table[targetSum];
}

// Test cases to validate the implementation
console.log(bestSum(7, [5, 3, 4, 7])); // Output: [ 7 ]
console.log(bestSum(8, [2, 3, 5])); // Output: [ 3, 5 ]
console.log(bestSum(8, [1, 4, 5])); // Output: [ 4, 4 ]
console.log(bestSum(100, [1, 2, 5, 25])); // Output: [ 25, 25, 25, 25 ]

/**
 * Explanation of the Code:
 * 1. We initialize a table with targetSum+1 elements, all set to null.
 * 2. We set the value at index 0 to an empty array, representing that a sum of 0 can be achieved with no numbers.
 * 3. We iterate through the table from 0 to targetSum.
 * 4. For each index with a valid combination, we iterate through the numbers array.
 * 5. For each number, we create a new combination by adding the number to the current combination.
 * 6. If the new combination is shorter than the current combination stored at index i + num, we update it.
 * 7. Finally, we return the shortest combination at index targetSum, or null if no valid combination is found.
 *
 * Related Subtopics:
 * - Memoization: Another dynamic programming approach using a top-down method with caching
 * - Space Optimization: Techniques to reduce space complexity in dynamic programming
 * - Common DP Problems: Coin change, knapsack problem, longest common subsequence, etc.
 */

