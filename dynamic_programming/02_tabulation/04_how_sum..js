/**
 * 03:53:02 - https://youtu.be/oBt53YbR9Kk?t=13982
 * 
 * 
 * Tabulation in Dynamic Programming:
 * - A bottom-up approach to solve problems by solving and storing solutions to all sub-problems
 * - Start with the smallest sub-problems and build up to the solution of the original problem
 * - This approach avoids the overhead of recursive calls and usually has better performance
 *
 * Problem: How Sum
 * - Given a targetSum and an array of numbers
 * - Determine any combination of elements that add up to exactly the targetSum
 * - If no combination adds up to targetSum, return null
 * - If multiple combinations are possible, return any single one
 * 
 * Time Complexity: O(m^2 * n) where m is the targetSum and n is the length of the numbers array
 * Space Complexity: O(m^2)
 *
 * Let's implement the how sum problem using Tabulation:
 */

function howSum(targetSum, numbers) {
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
                // Update the table at index i + num with a new combination that includes the current number
                // If adding num to i does not exceed targetSum
                if (i + num <= targetSum) {
                    table[i + num] = [...table[i], num];
                }
            }
        }
    }

    // Return the combination that adds up to targetSum, or null if no combination is found
    return table[targetSum];
}

// Test cases to validate the implementation
console.log(howSum(7, [2, 3])); // Output: [ 3, 2, 2 ]
console.log(howSum(7, [5, 3, 4, 7])); // Output: [ 4, 3 ]
console.log(howSum(7, [2, 4])); // Output: null
console.log(howSum(7, [2, 3, 5])); // Output: [ 3, 2, 2 ]
console.log(howSum(300, [7, 14])); // Output: null

/**
 * Explanation of the Code:
 * 1. We initialize a table with targetSum+1 elements, all set to null.
 * 2. We set the value at index 0 to an empty array, representing that a sum of 0 can be achieved with no numbers.
 * 3. We iterate through the table from 0 to targetSum.
 * 4. For each index with a valid combination, we iterate through the numbers array.
 * 5. For each number, if adding it to the current index does not exceed targetSum, we update the table at index i + num
 *    with a new array that includes the current number.
 * 6. Finally, we return the combination at index targetSum, or null if no valid combination is found.
 *
 * Related Subtopics:
 * - Memoization: Another dynamic programming approach using a top-down method with caching
 * - Space Optimization: Techniques to reduce space complexity in dynamic programming
 * - Common DP Problems: Coin change, knapsack problem, longest common subsequence, etc.
 */
