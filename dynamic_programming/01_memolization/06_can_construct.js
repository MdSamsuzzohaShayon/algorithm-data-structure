/**
 * 02:12:45 - https://youtu.be/oBt53YbR9Kk?t=7965
 * 
 * Problem:
 * Write a function `canConstruct(target, wordBank)` that accepts a target and an array of strings.
 * The function should return a boolean indicating whether or not the `target` can be constructed 
 * by concatenating elements of `wordBank` array.
 * You may reuse elements of `wordBank` as many times as needed.
 */

/**
 * Brute Force Approach
 * This function attempts to solve the problem using recursion without any optimizations.
 * @param {string} target - The target string we want to construct.
 * @param {string[]} wordBank - The array of words that can be used to construct the target.
 * @returns {boolean} - Returns true if the target can be constructed, otherwise false.
 */
function canConstruct(target, wordBank) {
    // Base case: If the target is an empty string, we can construct it by using zero words.
    if (target === '') {
        return true;
    }

    // Iterate over each word in the wordBank
    for (const word of wordBank) {
        // Check if the word is a prefix of the target
        if (target.indexOf(word) === 0) {
            // If it is, we create a new target by removing the prefix (word)
            const suffix = target.slice(word.length);
            // Recursively check if we can construct the new target (suffix) with the wordBank
            if (canConstruct(suffix, wordBank)) {
                return true;
            }
        }
    }

    // If no combination of words can construct the target, return false
    return false;
}

console.log("===== Brute Force =====");

// Brute Force
// m = target.length
// n = wordBank.length
// Time Complexity: O(n^m * m)
// In the worst case, we have to explore all combinations of the wordBank for each character in the target.
// Space Complexity: O(m^2)
// Due to the call stack and slicing of strings.
console.log(canConstruct('abcdef', ['ab', 'abc', 'cd', 'abcd'])); // true
console.log(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // false
console.log(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // true
console.log(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])); // false


/**
 * Optimized Approach using Memoization
 * This function optimizes the brute force approach by using memoization to store the results of subproblems.
 * @param {string} target - The target string we want to construct.
 * @param {string[]} wordBank - The array of words that can be used to construct the target.
 * @param {object} memo - An object used to store the results of subproblems.
 * @returns {boolean} - Returns true if the target can be constructed, otherwise false.
 */
function optimizedCanConstruct(target, wordBank, memo = {}) {
    // Check if the result for the current target is already in the memo
    if (target in memo) return memo[target];
    // Base case: If the target is an empty string, we can construct it by using zero words.
    if (target === '') return true;

    // Iterate over each word in the wordBank
    for (const word of wordBank) {
        // Check if the word is a prefix of the target
        if (target.indexOf(word) === 0) {
            // If it is, we create a new target by removing the prefix (word)
            const suffix = target.slice(word.length);
            // Recursively check if we can construct the new target (suffix) with the wordBank
            if (optimizedCanConstruct(suffix, wordBank, memo)) {
                // Store the result in the memo and return true
                memo[target] = true;
                return true;
            }
        }
    }

    // Store the result in the memo and return false
    memo[target] = false;
    return false;
}

console.log("===== Memoization =====");
// Memoization
// m = target.length
// n = wordBank.length
// Time Complexity: O(n * m^2)
// For each character in the target (m), we iterate over the wordBank (n) and slice the string (m).
// Space Complexity: O(m^2)
// Due to the memo object and the call stack.
console.log(optimizedCanConstruct('abcdef', ['ab', 'abc', 'cd', 'abcd'])); // true
console.log(optimizedCanConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // false
console.log(optimizedCanConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // true
console.log(optimizedCanConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])); // false
