// YouTube https://www.youtube.com/watch?v=EFXWgZJZqL8&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=18

/*
 * Problem - Given a **stored** array of 'n' elements and a target element 't', find the index of 't', in the array. Return  -1 if the target element is not found,
 * Binary search only works on sorted array. If there is not sorted array to work with use linear search or sort the array and use binary search
 *
 * arr = [-5, 2, 6, 4, 10], t = 10 -> should return 4
 * arr = [-5, 2, 6, 4, 10], t = 6 -> should return 3
 * arr = [-5, 2, 6, 4, 10], t = 20 -> should return -1
 *
 * Instructions
 * Figure out how to break down the problem into smaller version of the same problem,
 * Identify the base case for recursion
 *
 * Linear search pseurocode
 * If array is empty, return -1 as the element can not be found.
 * If the array has elements, find the middle element in the array. If target is equal to the middle element, return the middle element index.
 * If target element is less than the middle element, take only left half of the array
 * If target element is greater than the middle element, take only right half of the array
 */

function search(arr, target, leftI, rightI){
  if (leftI > rightI) return -1;

  let middleI = Math.floor((leftI + rightI) / 2);

  if (target === arr[middleI]) return middleI;

  if(target < arr[middleI]){
    return search(arr, target, leftI, middleI - 1);
  }else{
    return search(arr, target,  middleI + 1, rightI)
  }
}

function recursiveBinarySearch(arr, target){
  return search(arr, target, 0, arr.length - 1);
}

// Big-O = O(Log n)




const newArr = [-5, 2, 6, 4, 10];
console.log(recursiveBinarySearch(newArr, 10)); // Expected return // 4
console.log(recursiveBinarySearch(newArr, 6)); // Expected return // 2
console.log(recursiveBinarySearch(newArr, 20)); // Expected return // -1

// Big-O = O(log n)
