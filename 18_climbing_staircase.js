/*
 * YouTube - https://www.youtube.com/watch?v=jrY7eONLHZs&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=31
 *
 * Climbing Staircase
 * Problem - given a staircase of 'n' steps, count the number of distinct way to climb to the top. You can either climb 1 step or 2 steps at a time
 *
 * Example of the ways to calculate
 * n=1, climbingStaircase(1) = 1 ways          | (1)
 * n=2, climbingStaircase(2) = 2 ways          | (1, 1) and (2)
 * n=3, climbingStaircase(3) = 3 ways          | (1, 1, 1), (1,2) and (2,1)
 * n=4, climbingStaircase(4) = 5 ways          | (1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1)  and (2, 2)
 *
 * At any given time, you can climb either 1 step or 2 steps
 * That means if you have to climb to step 'n', we can only climb from step 'n-1' or 'n-2'
 * Calculate the ways we can climb to 'n-1' and 'n-2' steps and add the two
 * climbingStaircase(n) = climbingStaircase(n-1) + climbingStaircase(n-2)
 */

function climbingStaircase(n) {
  const numOfWays = [1, 2];

  for (let i = 2; i <= n; i++) {
    numOfWays[i] = numOfWays[i-1] + numOfWays[i-2];
  }

  return numOfWays[n - 1];
}

console.log(climbingStaircase(1)); // Expected return: 1
console.log(climbingStaircase(2)); // Expected return: 2
console.log(climbingStaircase(3)); // Expected return: 3
console.log(climbingStaircase(4)); // Expected return: 5
console.log(climbingStaircase(5)); // Expected return: 8


// Big-O = O(n)
