// Tutorial - https://www.youtube.com/watch?v=EFXWgZJZqL8&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=18

function search(arr, target, leftIdx, rightIdx) {
    if (leftIdx > rightIdx) return -1;

    const middleIdx = Math.floor((leftIdx + rightIdx) / 2);

    if (target === arr[middleIdx]) return middleIdx;

    if (target < arr[middleIdx]) {
        return search(arr, target, leftIdx, middleIdx - 1);
    }else{
        return search(arr, target, middleIdx + 1, rightIdx);
    }
}

function recursiveBinarySearch(arr, target) {
    return search(arr, target, 0, arr.length - 1);
}


const sArr = [-5, 2, 4, 6, 10];

console.log(recursiveBinarySearch(sArr, 10)); // 4
console.log(recursiveBinarySearch(sArr, 6)); // 3
console.log(recursiveBinarySearch(sArr, 20)); // -1


// Big-O = O(log n)