// YouTube https://www.youtube.com/watch?v=o5XweHW-H4Y&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=13

/*
 * Problem - Given an integer 'n', find the factorial of that integer
 * The factorial of a non-negative integer 'n', denoted n!, is the product of all posative integers less than or equal to 'n'
 * Factorial of zero is 1
 * factorial(4) = 4*3*2*1 = 24
 * factorial(5) = 5*4*3*2*1 = 120
 *
 * Let's say factorial symbol is !
 * 5! = 5*4*3*2*1              -> 5 * 4!
 * 4! = 4*3*2*1                -> 4 * 3!
 * 3! = 3*2*1                  -> 3 * 2!
 * 2! = 2*1                    -> 2 * 1!
 * 1! = 1*1                    -> 1 * 0!
 * 0! = 1
 *
 * n! = n * (n-1)!
 */


function recersiveFactorial(n){
  if (n === 0) return 1;
  return n * recursiveFactorial(n-1); // As n increases the number of execution increases at the same time
}


console.log(recursiveFactorial(0)); // Expected return: 1
console.log(recursiveFactorial(1)); // Expected return: 1
console.log(recursiveFactorial(5)); // Expected return: 120

// Big-O = O(n)
