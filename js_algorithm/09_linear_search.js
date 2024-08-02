// Tutorial - https://www.youtube.com/watch?v=EvRdNdOfRl8&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=15
function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i += 1) {
        if (arr[i] === target) return i;
    }
    return -1;
}


const sArr = [-5, 2, 10, 4, 6];

console.log(linearSearch(sArr, 10)); // 2
console.log(linearSearch(sArr, 6)); // 4
console.log(linearSearch(sArr, 20)); // -1

// Big-O = O(n)