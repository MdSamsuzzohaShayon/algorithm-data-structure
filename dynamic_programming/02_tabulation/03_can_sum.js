/**
 * 03:37:58 - https://youtu.be/oBt53YbR9Kk?t=13078
 * 
 * Problem:
 * Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.
 * The function should return a boolean indicating whether or not it is possi8ble to generate the targetSum using numbers from the array.
 * You may use an element of the array as many times as needed
 * You may assume that all input numbers are non-negative.
 */

function canSum(targetSum, numbers) {
    const table = new Array(targetSum + 1).fill(false);
    table[0] = true;

    for (let i = 0; i <= targetSum; i++) {
        if (table[i] === true) {
            for (const num of numbers) {
                table[i + num] = true;
            }
        }
    }

    return table[targetSum];
}

console.log(canSum(7, [2, 3])); // true
console.log(canSum(7, [5, 3, 4, 7])); // true
console.log(canSum(7, [2, 4])); // false
console.log(canSum(7, [2, 3, 5])); // true
console.log(canSum(300, [7, 14])); // false
// m = targetSum
// n = numbers.length
// O(mn) time complexity because of nested loop