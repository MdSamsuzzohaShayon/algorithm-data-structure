// https://www.youtube.com/watch?v=Oz4Y4psjG7w&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=11


function recursiveFibonacci(n) {
    if (n < 2) return n;
    return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
}



console.log(recursiveFibonacci(0));
console.log(recursiveFibonacci(1));
console.log(recursiveFibonacci(6));

// Big-O Interative: O(n)
// Big-O Recursive: O(n^2)