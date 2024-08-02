// Tutorial - https://www.youtube.com/watch?v=wXZyuJqNk9U&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=27


function merge(leftArr, rightArr){
    const sortedArr = [];
    while (leftArr?.length && rightArr?.length) {
        if(leftArr[0] <= rightArr[0]){
            sortedArr.push(leftArr.shift());
        }else{
            sortedArr.push(rightArr.shift());
        }
    }
    return [...sortedArr, ...leftArr, ...rightArr];
}

function mergeSort(arr){
    if(arr.length < 2) return arr;

    const mid = Math.floor(arr.length / 2);
    const leftArr = arr.slice(0, mid);
    const rightArr = arr.slice(mid);
    return merge(mergeSort(leftArr), mergeSort(rightArr));

}

const sArr = [8, 20, -2, 4, -6];
console.log(mergeSort(sArr));


// Big-O = O(n log n)  This is one of the best time complexity