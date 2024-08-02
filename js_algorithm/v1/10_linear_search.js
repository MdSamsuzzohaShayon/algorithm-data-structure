// YouTube https://www.youtube.com/watch?v=EvRdNdOfRl8&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=15

/*
 * Problem - given an array of 'n' elements and a target element 't', find the index of 't', in the array. Return  -1 if the target element is not found,
 * arr = [-5, 2, 10, 4, 6], t = 10 -> should return 2
 * arr = [-5, 2, 10, 4, 6], t = 6 -> should return 4
 * arr = [-5, 2, 10, 4, 6], t = 20 -> should return -1
 *
 * Linear search pseurocode
 * Start at the first element in the array and move towerds the last element
 * At each element though, check if the element is equal to the target element
 * If element found, return the index of the element
 * If element not found, return -1
 */

function linearSearch(arr, target){
  for (let i = 0; i < arr.length; i++) {
    if(arr[i] === target) return i;
  }
  return -1;
}


const newArr = [-5, 2, 10, 4, 6];
console.log(linearSearch(newArr, 10)); // Expected return: 2
console.log(linearSearch(newArr, 6)); // Expected return: 4
console.log(linearSearch(newArr, 20)); // Expected return: -1

// Big-O = O(n)
