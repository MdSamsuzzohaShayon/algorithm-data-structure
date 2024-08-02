// https://www.youtube.com/watch?v=3yUuo7TqMW8&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=4


function summation(n){
  let sum = 0; // Execute 1 time
  for (let i=1; i<= n; i++){
    sum += i // Execute 4 times
  }
  return sum ; // / Execute 1 time
  /*
   * n is the input to the function
   * So the total count is 4 + 2 (times executed)
   * If here n is 10 then total count will be 10 + 2
   * therefore, time complexity is dependent on the input size
   */
}

/*
 * If n is 100 then n + 2 = 102
 * If n is 1,000000 then n + 2 = 1,000002 at this point, 2 is very insignificant, we can usually drop it
 * Since n contributed to the most to the total value and not the additional 2
 * We do not have to cought up in the smaller steps that do not affect the performance as much as the others
 */
summation(4);


/*
 * O(n) - size of the input increases time complexity also increases
 * When there is a loop in the algorithm most of the time we can say time complexity is linear, but there are some exceptions
 * Loop's worst case is when it iterates over the entire input and hence the time complexity is linear
 */



// Time complexity of this algorithm is O(1) which is called constant time complexity
function summation2(n){
  return (n * (n+1)) / 2; // It executes only once no matter whatever the value of n is
}

console.log("Simulations 2 -> ", summation2(5));



/*
 * O(n^2)
 * Time complexity is Quadratic here
 */
const n = 4;
for (let i = 0; i < n; i++){
  for (let j = 0; j < i; j++){
    console.log(`I=${i}, J=${j}`)
  }
}




/*
 * O(n^3)
 * Time complexity is Cubic here
 * If input size reduces by half every iteration it is logarithmic
 */
for (let i = 0; i < n; i++){
  for (let j = 0; j < i; j++){
    for (let k = 0; k < j; k++){
      console.log(`I=${i}, J=${j}, K=${k}`)
    }
  }
}
