// YouTube https://www.youtube.com/watch?v=wZNxLwqxu00&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=12

/*
 * Problem - Given a number 'n', find the n^th element of the Fibonacci sequence
 * In mathematics, the Fibonacci sequence is a sequence in which each number is the sum of two preceding ones.
 * The first two numbers in the sequence are 0 and 1. (0, 1, 1, 2, 3, 5, 8...)
 */

 function recursiveFibonacci(n){
   /*
    * The Fibonacci sequence is a series of numbers where each number is the sum of the two before it.
    * This is because the Fibonacci sequence starts with 0 and 1 as the first two numbers
    * and then each subsequent number is the sum of the two preceding ones.
    */
   if ( n < 2 ) return n; // Break
   return recursiveFibonacci(n-1) + recursiveFibonacci(n-2);
 }


 // console.log(recursiveFibonacci(0)); // index 0
 // console.log(recursiveFibonacci(1)); // index 1

 console.log(recursiveFibonacci(6)); // index 8
 /*
 * First, it figures out the 5th number and the 4th number.
 * To find the 5th number, it does the same process: it finds the 4th and 3rd numbers.
 * It keeps going like this until it reaches the 0th and 1st numbers.
 * Then, it adds them all up to get the answer, which is 8 for the 6th number.
 */
 
 // console.log(recursiveFibonacci(7)); // (7 - 1) + (7 - 2) = index 13
 // Big-O = O(2^n) - Recursive solution
