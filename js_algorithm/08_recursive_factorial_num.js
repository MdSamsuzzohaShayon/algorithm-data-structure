// Tutorial:  https://www.youtube.com/watch?v=o5XweHW-H4Y&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=13

// Formula: n! = n * (n-1)!
function recursiveFactorial(n) {
    if (n === 0) return 1;
    return  n * recursiveFactorial(n - 1);
}


console.log("Factorial of number: ", recursiveFactorial(0))
console.log("Factorial of number: ", recursiveFactorial(1))
console.log("Factorial of number: ", recursiveFactorial(5))

// Big-O = O(n)