/**
 * 04:20:50 - https://youtu.be/oBt53YbR9Kk?t=15650
 * 
 * 
 * Tabulation in Dynamic Programming:
 * - A bottom-up approach to solve problems by solving and storing solutions to all sub-problems
 * - Start with the smallest sub-problems and build up to the solution of the original problem
 * - This approach avoids the overhead of recursive calls and usually has better performance
 *
 * Problem: Can Construct
 * - Given a target string and an array of strings (wordBank)
 * - Determine if the target string can be constructed by concatenating elements of the wordBank array
 * - Elements of wordBank can be reused as many times as needed
 * 
 * Time Complexity: O(m * n * k)
 * - m = length of target string
 * - n = length of wordBank array
 * - k = maximum length of any word in the wordBank
 * - The outer loop runs `m` times, and for each iteration, we check up to `n` words and slice up to `k` characters.
 *
 * Space Complexity: O(m)
 * - The table array stores `m + 1` boolean values.
 *
 * Let's implement the can construct problem using Tabulation:
 */

function canConstruct(target, wordBank) {
    // Create a table with target.length + 1 elements, initially filled with false
    const table = new Array(target.length + 1).fill(false);
    
    // There is exactly one way to construct an empty string: by using no words
    table[0] = true;

    // Iterate through each index of the table from 0 to target.length
    for (let i = 0; i <= target.length; i++) {
        // If the current index has a valid way to construct the substring
        if (table[i] === true) {
            // Iterate through each word in the wordBank array
            for (const word of wordBank) {
                // If the current word matches the substring starting at position i
                if (target.slice(i, i + word.length) === word) {
                    // Update the table at index i + word.length to true
                    table[i + word.length] = true;
                }
            }
        }
    }

    // Return whether it's possible to construct the entire target string
    return table[target.length];
}

// Test cases to validate the implementation
console.log(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])); // Output: true
console.log(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // Output: false
console.log(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // Output: true
console.log(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])); // Output: false

/**
 * Explanation of the Code:
 * 1. We initialize a table with target.length + 1 elements, all set to false.
 * 2. We set the value at index 0 to true, representing that an empty target string can be constructed with no words.
 * 3. We iterate through the table from 0 to target.length.
 * 4. For each index with a valid construction (true), we iterate through the wordBank array.
 * 5. For each word, we check if it matches the substring of the target starting at index `i`.
 * 6. If it matches, we update the table at index i + word.length to true.
 * 7. Finally, we return the value at index target.length, indicating if the entire target string can be constructed.
 *
 * Related Subtopics:
 * - Memoization: Another dynamic programming approach using a top-down method with caching
 * - Space Optimization: Techniques to reduce space complexity in dynamic programming
 * - Common DP Problems: Coin change, knapsack problem, longest common subsequence, etc.
 */
