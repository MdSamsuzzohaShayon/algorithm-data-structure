// https://youtu.be/cbHMQxOuIUw?list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa

function isPrime(n){
    if(n < 2) return false;

    for (let i = 2; i < n; i++) {
        if(n%i === 0 ){
            return false;
        }
    }
    return true;
}


console.log(isPrime(1)); // false
console.log(isPrime(5)); // true
console.log(isPrime(4)); // false

// isPrime(5) = true(1*5 or 5*1)
// isPrime(4) = true(1*4 or 4*1 or 2*2)


// Big-O = O(n)



function isOptimalPrime(n){
    if(n < 2) return false;

    for (let i = 2; i <= Math.sqrt(n); i++) {
        if(n%i === 0){
            return false;
        }
    }
    return true;
}

console.log("\n\nOptimal solution =================================");
console.log(isOptimalPrime(1)); // false
console.log(isOptimalPrime(5)); // true
console.log(isOptimalPrime(4)); // false
// Big-O = O(sqrt(n))