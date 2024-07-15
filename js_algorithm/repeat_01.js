function summation(n){
    let sum = 0;
    for(let i = 1; i < n; i+=1){
        sum += i;
    }
    return sum
}

console.log(summation(4));

// Big-O = O(n) Linear