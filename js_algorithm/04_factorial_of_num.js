// https://www.youtube.com/watch?v=vAgzuS3u6W0&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=8

function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

console.log(factorial(0));// Factorial of zero is 1
console.log(factorial(4));// factorial(4) = 4*3*2*1 = 24
console.log(factorial(5)); // factorial(5) = %*4*3*2*1 = 120

// Big-O = O(n)