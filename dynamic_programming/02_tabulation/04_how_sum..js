/**
 * 03:53:02 - https://youtu.be/oBt53YbR9Kk?t=13982
 * 
 * Problem:
 * Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.
 * The function should return an array containing any combination of elements that add up to exactly the targetSum.
 * If there is no combination that adds up to the targetSum, then return null.
 * If there are multiple combinations possible, you may return any single one.
 */

function howSum(targetSum, numbers){
    const table = new Array(targetSum + 1).fill(null);
    table[0]=[];

    for (let i = 0; i <= targetSum; i++) {
        if(table[i] !== null){
            for (const num of numbers) {
                table[i+num] = [...table[i], num];
            }
        }
    }

    return table[targetSum];
}


console.log(howSum(7, [2, 3])); // Output: [ 3, 2, 2 ]
console.log(howSum(7, [5, 3, 4, 7])); // Output: [ 4, 3 ]
console.log(howSum(7, [2, 4])); // Output: null
console.log(howSum(7, [2, 3, 5])); // Output: [ 3, 2, 2 ]
console.log(howSum(300, [7, 14])); // Output: null
// m = targetSum
// n = numbers.length
// Big-O = O(m^2 * n) Time
// Big-O = O(m^2) Space