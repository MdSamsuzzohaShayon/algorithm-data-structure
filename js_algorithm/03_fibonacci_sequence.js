// https://www.youtube.com/watch?v=tQjd29Rmo_A&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=7


function fibonacci(n) {
    const fib = [0, 1];
    for (let i = 2; i < n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib;
}

console.log(fibonacci(1)); // [0,1]
console.log(fibonacci(2)); // [0,1]
console.log(fibonacci(3)); // [0,1, 1]
console.log(fibonacci(7)); // [0,1, 1, 2, 3, 5, 8]

// Big-O = O(n)