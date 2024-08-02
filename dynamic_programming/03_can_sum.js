/**
 * 01:04:52 - https://youtu.be/oBt53YbR9Kk?t=3895
 * 
 * Memoizatin recipe
 *      1. Make it work
 *          - Visualize the problem as a tree
 *          - Implement the tree using recursion
 *          - Test it
 *      2. Make it efficient
 *          - Add a memo object
 *          - Add a base case to return memo values
 *          - Store return values into the memo
 * 
 * 
 * 
 * Problem: 
 * Write a function `canSum(targetSum, numbers)` that takies in a targetSum and an array of numbers as arguments.
 * The function should return a boolean indicating weether or not it is possible to generate the targetSum suing numbers from the array.
 * You may use an element of the array as many times as needed.
 * You may assume that all inpu numbers are non-negative.
 * 
 * Example 1: 
 *          Input: canSum(7, [5, 3, 4, 7])
 *          Output: true 
 *          (it is possible to to generate 7 by adding 3 + 4. Moreover, we can take 7 itself because 7 is a member of the array)
 */

function canSum(targetSum, numbers){
    if(targetSum === 0) return true;
    if (targetSum < 0) return false;

    for (const num of numbers) {
        const remainder =  targetSum - num;

        if(canSum(remainder, numbers) === true) return true;
    }

    return false;
}
// Brute Force
// n = array length and m = target sum
// Big-O = O(n^m) time complexity
// Big-O = O(m) space complexity

console.log("===== Brute Force =====");
console.log(canSum(7, [2, 3])); // true
console.log(canSum(7, [5, 3, 4, 7])); // true
console.log(canSum(7, [2, 4])); // false
console.log(canSum(8, [2, 3, 5])); // true
console.log(canSum(300, [7, 14])); // true




function optimizedCanSum(targetSum, numbers, memo={}){
    if (targetSum in memo) return memo[targetSum];
    if(targetSum === 0) return true;
    if (targetSum < 0) return false;

    for (const num of numbers) {
        const remainder =  targetSum - num;

        if(optimizedCanSum(remainder, numbers, memo) === true){
            memo[targetSum] = true;
            return true;
        }
    }
    memo[targetSum] = false;
    return false;
}

console.log("===== Memoization =====");
console.log(optimizedCanSum(7, [2, 3])); // true
console.log(optimizedCanSum(7, [5, 3, 4, 7])); // true
console.log(optimizedCanSum(7, [2, 4])); // false
console.log(optimizedCanSum(8, [2, 3, 5])); // true
console.log(optimizedCanSum(300, [7, 14])); // true
// Memoized
// n = array length and m = target sum
// Big-O = O(n*m) time complexity
// Big-O = O(m) space complexity