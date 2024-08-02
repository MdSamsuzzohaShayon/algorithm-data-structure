/**
 * Grid Traveler - Memoization
 * 00:38:40 - https://youtu.be/oBt53YbR9Kk?t=2321
 * 
 * Say that ypu are a traveler on a 2D grid. You begain in the top-left corner and your goal is to travel to the bottom-right corner. 
 * You may only move down or right.
 * In how many ways can you travel to the goal on a grid with dimensions m*n?
 * 
 * Write a function `gridTraveler(m,n)` that calculates this.
 */

function gridTraveler(m, n) {
    if (m === 1 && n === 1) return 1;
    if (m === 0 || n === 0) return 0;
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1);
}
// Brute force
// Time complexity is Big-O = O(2^n+m)
// Space complexity is Big-O = O(n+m)

console.log(gridTraveler(1, 1,)); // 1
console.log(gridTraveler(2, 3)); // 3
console.log(gridTraveler(3, 2)); // 3
console.log(gridTraveler(3, 3)); // 6
console.log(gridTraveler(16, 16)); // 155117520



function optimizedGridTraveler(m, n, memo={}) {
    const key = `${m},${n}`;
    if(key in memo) return memo[key];
    if (m === 1 && n === 1) return 1;
    if (m === 0 || n === 0) return 0;
    memo[key] = optimizedGridTraveler(m - 1, n, memo) + optimizedGridTraveler(m, n - 1, memo);
    return memo[key]
}
// Memorized
// Time complexity is Big-O = O(n*m)
// Space complexity is Big-O = O(n+m)

console.log(optimizedGridTraveler(1, 1,)); // 1
console.log(optimizedGridTraveler(2, 3)); // 3
console.log(optimizedGridTraveler(3, 2)); // 3
console.log(optimizedGridTraveler(3, 3)); // 6
console.log(optimizedGridTraveler(16, 16)); // 155117520