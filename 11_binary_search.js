// YouTube https://www.youtube.com/watch?v=oVj5ZvZd-cU&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=16

/*
 * Problem - Given a **stored** array of 'n' elements and a target element 't', find the index of 't', in the array. Return  -1 if the target element is not found,
 * Binary search only works on sorted array. If there is not sorted array to work with use linear search or sort the array and use binary search
 *
 * arr = [-5, 2, 6, 4, 10], t = 10 -> should return 4
 * arr = [-5, 2, 6, 4, 10], t = 6 -> should return 3
 * arr = [-5, 2, 6, 4, 10], t = 20 -> should return -1
 *
 * Linear search pseurocode
 * If array is empty, return -1 as the element can not be found.
 * If the array has elements, find the middle element in the array. If target is equal to the middle element, return the middle element index.
 * If target is less than middle element, binary search oeft half of the array.
 * If target is greater than middle element, binary search right half of the array.
 */

function binarySearch(arr, target){
  let leftIndex = 0;
  let rightIndex = arr.length - 1;

  while (leftIndex <= rightIndex){
    let middleIndex = Math.floor((leftIndex + rightIndex) / 2);
    if(target === arr[middleIndex]) return middleIndex;

    if(target < arr[middleIndex]){
      rightIndex = middleIndex - 1;
    }else{
      leftIndex = middleIndex + 1;
    }
  }

  return -1;
}


const newArr = [-5, 2, 6, 4, 10];
console.log(binarySearch(newArr, 10)); // Expected return // 4
console.log(binarySearch(newArr, 6)); // Expected return // 3
console.log(binarySearch(newArr, 20)); // Expected return // -1

// Big-O = O(log n)
