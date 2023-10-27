// YouTube - https://www.youtube.com/watch?v=vAgzuS3u6W0&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=8

/*
 * Problem - Given a integer 'n', find the factorial of that integer
 * In mathematic, the factorial of a non-negative integer 'n', denoted n!, is the product of all positive integers less than or equal to 'n'
 * Factorial of zero is 1
 * Example 1: factorial(4) = 4 * 3 * 2 * 1 = 24
 * Example 2: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
 */


function factorial(n){
  let result = 1;
  // Since multiplying by 1 has not effect therefore we are starting from index 2 in the loop
  for (let i = 2; i <= n; i++) {
    console.log({result: result, i, result_mul_i: result * i});
    result = result * i;
  }
  return result;
}

console.log(factorial(0)); // Expected return: 1
console.log(factorial(1)); // Expected return: 1
console.log(factorial(5)); // Expected return: 120

/*
 * Big-O = O(n) Linear
 * As value o n increases this line execution increases therefore, this is linear time complexity
 */
