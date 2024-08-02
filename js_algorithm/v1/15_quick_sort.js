/*
 * YouTube - https://www.youtube.com/watch?v=ceqwscS_muA&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=24
 *
 * Problem - Given an array of integers, sort the array
 *
 * Adentify the pivot element in the array
 *    Method-1: Pick first element as pivot
 *    Method-2: Pick last element as pivot (Use this method)
 *    Method-3: Pick random element as pivot
 *    Method-4: Pick median as pivot
 * Put everything that is smaller than the pivot into a left array and everything that is greater than the pivot into right array
 * Repeat the process for the individual left and right arrays till you have an array of length 1 which is sorted by defination
 * Repeatedly concatenate the left array, pivort and right arry till one sorted array remains
 */



function quickSort(arr){
    if (arr.length < 2) return arr;
    let pivot = arr[arr.length - 1];
    let left = [];
    let right = [];
    for (var i = 0; i < arr.length - 1; i++) {
      arr[i] < pivot ? left.push(arr[i]) : right.push(arr[i]);
    }
    return [...quickSort(left), pivot, ...quickSort(right)];
}


const arr = [8, 20, -2, 4, -6];
console.log(quickSort(arr)); // Expected return: [-6, -2, 4, 8, 20];

/*
 * Worst case senario: O(n^2)
 * Average case: O(n log n)
 */
