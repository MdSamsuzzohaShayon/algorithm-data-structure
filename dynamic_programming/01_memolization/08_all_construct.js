/**
 * 02:47:30 - https://youtu.be/oBt53YbR9Kk?t=10050
 *
 * 
 * Problem: 
 * Write a function `allConstruct(target, wordBank)` that accepts a target string and an array of strings.
 * This function should return a 2D array containing all the ways that `target` can be constructed by concatenating elements of the `wordBank` array.
 * Each element of the 2D array should represent one combination that constructs the `target`
 * You may reuse elements of `wordBank` as many times as needed.
 */

/**
 * Brute Force Approach
 * This function attempts to solve the problem using recursion without any optimizations.
 * @param {string} target - The target string we want to construct.
 * @param {string[]} wordBank - The array of words that can be used to construct the target.
 * @returns {string[][]} - Returns a 2D array containing all the ways to construct the target.
 */
function allConstruct(target, wordBank) {
    // Base case: If the target is an empty string, return an array containing an empty array
    if (target === '') return [[]];

    const result = [];

    // Iterate over each word in the wordBank
    for (const word of wordBank) {
        // Check if the word is a prefix of the target
        if (target.indexOf(word) === 0) {
            // If it is, we create a new target by removing the prefix (word)
            const suffix = target.slice(word.length);
            // Recursively find all ways to construct the suffix
            const suffixWays = allConstruct(suffix, wordBank);
            // For each way to construct the suffix, add the current word to the beginning
            const targetWays = suffixWays.map(way => [word, ...way]);
            // Add all the ways to construct the target to the result array
            result.push(...targetWays);
        }
    }

    return result;
}

// Brute Force
// m = target.length
// n = wordBank.length
// Time Complexity: O(n^m)
// Each recursive call spawns n new recursive calls, leading to exponential time complexity.
// Space Complexity: O(m)
// The maximum depth of the recursion tree is m.
console.log("===== Brute Force =====");
console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])); // [ [ 'purp', 'le' ], [ 'p', 'ur', 'p', 'le' ] ]
console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])); // [ [ 'ab', 'cd', 'ef' ], [ 'ab', 'c', 'def' ], [ 'abc', 'def' ], [ 'abcd', 'ef' ] ]
console.log(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // []
console.log(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa'])); // []

/**
 * Optimized Approach using Memoization
 * This function optimizes the brute force approach by using memoization to store the results of subproblems.
 * @param {string} target - The target string we want to construct.
 * @param {string[]} wordBank - The array of words that can be used to construct the target.
 * @param {object} memo - An object used to store the results of subproblems.
 * @returns {string[][]} - Returns a 2D array containing all the ways to construct the target.
 */
function optimizedAllConstruct(target, wordBank, memo = {}) {
    // Check if the result for the current target is already in the memo
    if (target in memo) return memo[target];
    // Base case: If the target is an empty string, return an array containing an empty array
    if (target === '') return [[]];

    const result = [];

    // Iterate over each word in the wordBank
    for (const word of wordBank) {
        // Check if the word is a prefix of the target
        if (target.indexOf(word) === 0) {
            // If it is, we create a new target by removing the prefix (word)
            const suffix = target.slice(word.length);
            // Recursively find all ways to construct the suffix
            const suffixWays = optimizedAllConstruct(suffix, wordBank, memo);
            // For each way to construct the suffix, add the current word to the beginning
            const targetWays = suffixWays.map(way => [word, ...way]);
            // Add all the ways to construct the target to the result array
            result.push(...targetWays);
        }
    }

    // Store the result in the memo and return the total count
    memo[target] = result;
    return result;
}

console.log("===== Memoization =====");
// Memoization
// m = target.length
// n = wordBank.length
// Time Complexity: O(n * m)
// Each target string can be constructed in a number of ways proportional to its length, leading to polynomial time complexity.
// Space Complexity: O(m)
// Due to the memo object and the call stack.
console.log(optimizedAllConstruct("purple", ["purp", "p", "ur", "le", "purpl"])); // [ [ 'purp', 'le' ], [ 'p', 'ur', 'p', 'le' ] ]
console.log(optimizedAllConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])); // [ [ 'ab', 'cd', 'ef' ], [ 'ab', 'c', 'def' ], [ 'abc', 'def' ], [ 'abcd', 'ef' ] ]
console.log(optimizedAllConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // []
console.log(optimizedAllConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa'])); // []
