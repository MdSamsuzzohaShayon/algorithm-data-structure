/**
 * 02:12:45 - https://youtu.be/oBt53YbR9Kk?t=7965
 * 
 * Problem:
 * Write a function `canConstruct(target, wordBank)` that accepts a target and an array of strings
 * The function should return a boolen indicating whether or not the `target` can be constructed by concatenating elements of `wordBank` array.
 * You may reuse elements of `wordBank` as many times as needed.
 */


function canConstruct(target, wordBank){
    if(target === '') {
        return true;
    }

    for (const word of wordBank) {
        if(target.indexOf(word) === 0){
            const suffix = target.slice(word.length);
            if(canConstruct(suffix, wordBank)){
                return true;
            }
        }
    }

    return false;
}
console.log("===== Brute Force =====");

// Brute Force
// m = target.length
// n = wordBank.length
// Time Complexity O(n^m*m)
// Space Complexity O(m*m)
console.log(canConstruct('abcdef', ['ab', 'abc', 'cd', 'abcd'])); // true
console.log(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // false
console.log(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // true
console.log(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])); // false



function optimizedCanConstruct(target, wordBank, memo={}){
    if(target in memo) return memo[target];
    if(target === '') return true;

    for (const word of wordBank) {
        if(target.indexOf(word) === 0){
            const suffix = target.slice(word.length);
            if(optimizedCanConstruct(suffix, wordBank, memo)){
                memo[target] = true;
                return true;
            }
        }
    }

    memo[target] = false;
    return false;
}

console.log("===== Memolization =====");
// Memolization
// m = target.length
// n = wordBank.length
// Time Complexity O(n*m*m)
// Space Complexity O(m*m)
console.log(optimizedCanConstruct('abcdef', ['ab', 'abc', 'cd', 'abcd'])); // true
console.log(optimizedCanConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])); // false
console.log(optimizedCanConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])); // true
console.log(optimizedCanConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])); // false
