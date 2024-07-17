// Tutorial - https://youtu.be/jrY7eONLHZs?list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa

// Formula: climbingStair(n) = climbingStair(n-1) + climbingStair(n-2)

function climbingStair(n){
    const noOfWays = [1, 2];
    for (let i = 2; i <= n; i++) {
        noOfWays[i] = noOfWays[i - 1] + noOfWays[i - 2];
    }
    return noOfWays[n - 1];
}


console.log(climbingStair(1));
console.log(climbingStair(2));
console.log(climbingStair(4));
console.log(climbingStair(5));
console.log(climbingStair(6));