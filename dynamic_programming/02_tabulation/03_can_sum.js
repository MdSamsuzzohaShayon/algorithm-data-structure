/**
 * 03:37:58 - https://youtu.be/oBt53YbR9Kk?t=13078
 * 
 * 
 * Tabulation in Dynamic Programming:
 * - A bottom-up approach to solve problems by solving and storing solutions to all sub-problems
 * - Start with the smallest sub-problems and build up to the solution of the original problem
 * - This approach avoids the overhead of recursive calls and usually has better performance
 *
 * Problem: Can Sum
 * - Given a targetSum and an array of numbers
 * - Determine if it's possible to generate the targetSum using the numbers from the array
 * - You may use each number as many times as needed
 * - All input numbers are non-negative
 * 
 * Time Complexity: O(mn) where m is the targetSum and n is the length of the numbers array
 * Space Complexity: O(m)
 *
 * Let's implement the can sum problem using Tabulation:
 */

function canSum(targetSum, numbers) {
    // Create a table with targetSum+1 elements, initially filled with false
    const table = new Array(targetSum + 1).fill(false);
    
    // There is exactly one way to reach a targetSum of 0: by using no numbers
    table[0] = true;

    // Iterate through each index of the table from 0 to targetSum
    for (let i = 0; i <= targetSum; i++) {
        // If it's possible to reach the current sum `i`
        if (table[i] === true) {
            // Iterate through each number in the array
            for (const num of numbers) {
                // If we can reach the sum `i`, then we can also reach the sum `i + num`
                if (i + num <= targetSum) {
                    table[i + num] = true;
                }
            }
        }
    }

    // Return whether it's possible to reach the targetSum
    return table[targetSum];
}

// Test cases to validate the implementation
console.log(canSum(7, [2, 3])); // Output: true
console.log(canSum(7, [5, 3, 4, 7])); // Output: true
console.log(canSum(7, [2, 4])); // Output: false
console.log(canSum(7, [2, 3, 5])); // Output: true
console.log(canSum(300, [7, 14])); // Output: false

/**
 * Explanation of the Code:
 * 1. We initialize a table with targetSum+1 elements, all set to false.
 * 2. We set the value at index 0 to true, as there is one way to achieve a sum of 0: use no numbers.
 * 3. We iterate through the table from 0 to targetSum.
 * 4. For each index where the value is true, we iterate through the numbers array.
 * 5. For each number, if adding it to the current index does not exceed targetSum, we set the corresponding index in the table to true.
 * 6. Finally, we return the value at index targetSum, indicating if the targetSum can be achieved.
 *
 * Related Subtopics:
 * - Memoization: Another dynamic programming approach using a top-down method with caching
 * - Space Optimization: Techniques to reduce space complexity in dynamic programming
 * - Common DP Problems: Coin change, knapsack problem, longest common subsequence, etc.
 */
