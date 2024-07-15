// https://www.youtube.com/watch?v=3yUuo7TqMW8&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa&index=4


function summation(n) {
    let sum = 0; // Execute 1 time
    for (let i = 1; i <= n; i++) {
        sum += i // Execute 4 times
    }
    return sum; // / Execute 1 time
}
summation(4);


// Time complexity of this algorithm is O(1) which is called constant time complexity
function summation2(n) {
    return (n * (n + 1)) / 2; // It executes only once no matter whatever the value of n is
}


const n = 4;
for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
        console.log(`I=${i}, J=${j}`)
    }
}




for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
        for (let k = 0; k < j; k++) {
            console.log(`I=${i}, J=${j}, K=${k}`)
        }
    }
}
