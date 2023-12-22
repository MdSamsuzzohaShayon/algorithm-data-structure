/*
 * YouTube https://www.youtube.com/watch?v=Wu_mDUIsTVE&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=22
 *
 * Virtually split the array into a sorted and an unsorted part
 * Assume that the first element is already sorted and remaining elements are unsorted
 * Select an unsorted element and compare with all elements in the sorted part
 * If the elements in the sorted part is smaller than the selected element process to the next element in the unsorted part. Else, shift larget element in the sorted part towards the right
 * Insert the selected element at the right index
 * Repeat till all the unsorted elements are placed in the right order
 */


function insertionSort(arr){
  for (let i = 1; i < arr.length; i++ ) {
    let numToInsert = arr[i];
    let j = i - 1; // Index of sorted element
    // Sorted element can be more than 1 - all than element that is greater than number to insert are shifted to right
    while (j >= 0 && arr[j] > numToInsert) {
      arr[j+1] = arr[j];
      j = j - 1;
    }
    arr[j+1] = numToInsert;
  }
}

const arr = [8, 20, -2, 4, -6];
insertionSort(arr);
console.log(arr); // Expected return: [-6, -3, 4, 8, 20]

// Big-O = O(n^2)
