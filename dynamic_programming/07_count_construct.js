/**
 * 02:38:35 - https://youtu.be/oBt53YbR9Kk?t=9515
 * 
 * Problem:
 * Write a function `countConstruct(target, wordBank)` that accepts a target string and an array of strings.
 * The function should return the number of ways that the `target` can be constructed by concatenating elements of the `wordBank` array.
 * You may reuse elements of `wordBank` as many times as needed.
 */


function countConstruct(target, wordBank){
    if(target === '') return 1;
    let totalCount = 0;

    for (const word of wordBank) {
        if(target.indexOf(word) === 0){
            const numWaysForRest = countConstruct(target.slice(word.length), wordBank);
            totalCount += numWaysForRest;
        }
    }

    return totalCount;
}
console.log("===== Brute Force =====");

// Brute Force
// m = target.length
// n = wordBank.length
// Time Complexity O(n^m*m)
// Space Complexity O(m*m)
console.log(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])); // 2
console.log(countConstruct('abcdef', ['ab', 'abc', 'cd', 'abcd'])); // 1
console.log(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // 0
console.log(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // 4
console.log(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])); // 0



function optimizedCountConstruct(target, wordBank, memo={}){
    if(target in memo) return memo[target];
    if(target === '') return 1;
    let totalCount = 0;

    for (const word of wordBank) {
        if(target.indexOf(word) === 0){
            const numWaysForRest = optimizedCountConstruct(target.slice(word.length), wordBank, memo);
            totalCount += numWaysForRest;
        }
    }

    memo[target] = totalCount;
    return totalCount;
}
console.log("===== Memolization =====");

// Memolization
// m = target.length
// n = wordBank.length
// Time Complexity O(n*m*m)
// Space Complexity O(m*m)
console.log(optimizedCountConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])); // 2
console.log(optimizedCountConstruct('abcdef', ['ab', 'abc', 'cd', 'abcd'])); // 1
console.log(optimizedCountConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // 0
console.log(optimizedCountConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // 4
console.log(optimizedCountConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])); // 0
