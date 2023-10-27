// YouTube - https://www.youtube.com/watch?v=cbHMQxOuIUw&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=9

/*
 * Problem - Given a nautral 'n', determine if the number is prime or not
 * A prime number is a natural number grater than 1 that is not a product of two smaller natural numbers.
 * Example 1: isPrime(5) = true (1*5 or 5*1)
 * Example 2: isPrime(4) = false (1*4 or 2*2 or 4*1)
 */

function isPrime(n){
  // Prime number is a natural number greater than 1
  if( n < 2) return false
  for (let i = 2; i < n; i++) {
    console.log({i, n, n_i_modulas: n%i});
    if (n%i === 0)  return false; // As value o n increases this line execution increases therefore, this is linear time complexity
  }
  return true;
}

console.log("Result for isPrime(1) - ", isPrime(1)); // Expected return: false
console.log("Result for isPrime(5) - ", isPrime(5)); // Expected return: true
console.log("Result for isPrime(4) - ", isPrime(4)); // Expected return: false

// Big-O = O(n) Linear
