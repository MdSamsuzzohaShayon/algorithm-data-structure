/*
 * YouTube - https://www.youtube.com/watch?v=C2HuBFYgyM8&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=29
 *
 * Cartesian product
 * Problem - given two finite non-empty sets, find their cartesian Product.
 * In Mathematics, specifically set theory, the Cartesian product of two sets A and B, denoted AxB, is the set of all ordered pairs (a,b) where a is in A and b is in B
 *
 * Example
 * A = [1,2]
 * B = [3,4]
 * A x B = [[1,3], [1,4], [2,3], [2,4]]
 *
 * Traverse each array and pair each element in the first array with each element in the second array
 */


function cartesianProduct(arr1, arr2) {
  const result = [];

  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr2.length; j++) {
      result.push([arr1[i], arr2[j]]);
    }
  }

  return result;
}

const arr1 = [1,2];
const arr2 = [3,4,5];
console.log(cartesianProduct(arr1, arr2)); // Expected result: [[1,3], [1,4], [1,5], [2,3], [2,4], [2,5]]


/*
 * Since in this case two are can be with different length it will not going to be O(n^2)
 * Big-O = O(mn)
 */
