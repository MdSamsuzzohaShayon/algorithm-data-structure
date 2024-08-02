/**
 * 00:02:43 - https://youtu.be/oBt53YbR9Kk?t=223
 * 
 * Write a function `fib(n)` that takes in a number as an argument. The function should return the n-th number of the fibonacci sequence.
 * The 1st and 2nd number of the sequence is 1. To generate the next number of the sequence, we sum the previous 2.
 */

function addCommas(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

const fib=(n)=>{
    if(n<= 2) return 1;
    return fib(n-1) + fib(n-2);
}
// Big-O = O(2^n)
console.log(fib(4));
console.log(fib(5));
console.log(fib(10));

console.log("==========Before Optimization==========");
let dateTime = new Date();
console.log(`Start ${dateTime.getMinutes()} minutes and ${dateTime.getSeconds()} seconds `);
console.log(fib(45)); // This lacks in efficiency and take plenty of time executing a large number
dateTime = new Date();
console.log(`End ${dateTime.getMinutes()} minutes and ${dateTime.getSeconds()} seconds `);

// 00:23:43 - https://youtu.be/oBt53YbR9Kk?t=1424
// Optimize the performance using Memoization / Dynamic programming
const optimizedFib=(n, memo={})=>{
    if (n in memo) return memo[n];
    if(n<= 2) return 1;
    memo[n] = optimizedFib(n-1, memo) + optimizedFib(n-2, memo);
    return memo[n]
}

console.log("==========After Optimization==========");
dateTime = new Date();
console.log(`Start ${dateTime.getMinutes()} minutes and ${dateTime.getSeconds()} seconds `);
console.log(optimizedFib(45)); // This lacks in efficiency and take plenty of time executing a large number
dateTime = new Date();
console.log(`End ${dateTime.getMinutes()} minutes and ${dateTime.getSeconds()} seconds `);
// Big-O = O(2) For time and space complexity