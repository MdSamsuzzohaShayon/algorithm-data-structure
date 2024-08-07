/**
 * 02:38:35 - https://youtu.be/oBt53YbR9Kk?t=9515
 * 
 * Problem:
 * Write a function `countConstruct(target, wordBank)` that accepts a target string and an array of strings.
 * The function should return the number of ways that the `target` can be constructed by concatenating elements of the `wordBank` array.
 * You may reuse elements of `wordBank` as many times as needed.
 */

/**
 * Brute Force Approach
 * This function attempts to solve the problem using recursion without any optimizations.
 * @param {string} target - The target string we want to construct.
 * @param {string[]} wordBank - The array of words that can be used to construct the target.
 * @returns {number} - Returns the number of ways the target can be constructed.
 */
function countConstruct(target, wordBank) {
    // Base case: If the target is an empty string, there is one way to construct it (by using no words).
    if (target === '') return 1;

    let totalCount = 0;

    // Iterate over each word in the wordBank
    for (const word of wordBank) {
        // Check if the word is a prefix of the target
        if (target.indexOf(word) === 0) {
            // If it is, we create a new target by removing the prefix (word)
            const numWaysForRest = countConstruct(target.slice(word.length), wordBank);
            // Add the number of ways to construct the rest of the target to the total count
            totalCount += numWaysForRest;
        }
    }

    return totalCount;
}

console.log("===== Brute Force =====");

// Brute Force
// m = target.length
// n = wordBank.length
// Time Complexity: O(n^m * m)
// In the worst case, we have to explore all combinations of the wordBank for each character in the target.
// Space Complexity: O(m^2)
// Due to the call stack and slicing of strings.
console.log(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])); // 2
console.log(countConstruct('abcdef', ['ab', 'abc', 'cd', 'abcd'])); // 1
console.log(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // 0
console.log(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // 4
console.log(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])); // 0

/**
 * Optimized Approach using Memoization
 * This function optimizes the brute force approach by using memoization to store the results of subproblems.
 * @param {string} target - The target string we want to construct.
 * @param {string[]} wordBank - The array of words that can be used to construct the target.
 * @param {object} memo - An object used to store the results of subproblems.
 * @returns {number} - Returns the number of ways the target can be constructed.
 */
function optimizedCountConstruct(target, wordBank, memo = {}) {
    // Check if the result for the current target is already in the memo
    if (target in memo) return memo[target];
    // Base case: If the target is an empty string, there is one way to construct it (by using no words).
    if (target === '') return 1;

    let totalCount = 0;

    // Iterate over each word in the wordBank
    for (const word of wordBank) {
        // Check if the word is a prefix of the target
        if (target.indexOf(word) === 0) {
            // If it is, we create a new target by removing the prefix (word)
            const numWaysForRest = optimizedCountConstruct(target.slice(word.length), wordBank, memo);
            // Add the number of ways to construct the rest of the target to the total count
            totalCount += numWaysForRest;
        }
    }

    // Store the result in the memo and return the total count
    memo[target] = totalCount;
    return totalCount;
}

console.log("===== Memoization =====");
// Memoization
// m = target.length
// n = wordBank.length
// Time Complexity: O(n * m^2)
// For each character in the target (m), we iterate over the wordBank (n) and slice the string (m).
// Space Complexity: O(m^2)
// Due to the memo object and the call stack.
console.log(optimizedCountConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])); // 2
console.log(optimizedCountConstruct('abcdef', ['ab', 'abc', 'cd', 'abcd'])); // 1
console.log(optimizedCountConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // 0
console.log(optimizedCountConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // 4
console.log(optimizedCountConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])); // 0
