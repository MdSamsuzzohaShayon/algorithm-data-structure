// Tutorial - https://www.youtube.com/watch?v=oVj5ZvZd-cU&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=16
// Binary search only works on sorted array
function binarySearch(arr, target){
    let leftIdx = 0,
    rightIdx = arr.length - 1;

    while (leftIdx <= rightIdx){
        const middleIdx = Math.floor((leftIdx + rightIdx) / 2);
        if(target === arr[middleIdx]) return middleIdx;
        if (target < arr[middleIdx]){
            rightIdx = middleIdx - 1;
        }else{
            leftIdx = middleIdx + 1;
        }
    }
    return -1;
}


const sArr = [-5, 2, 4, 6, 10];

console.log(binarySearch(sArr, 10)); // 4
console.log(binarySearch(sArr, 6)); // 3
console.log(binarySearch(sArr, 20)); // -1

// Big-O = O(log n)
