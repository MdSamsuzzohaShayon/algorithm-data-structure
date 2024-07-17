// Tutorial - https://youtu.be/_dt773ImwFw?si=klTEMF7mtd_c4XFc

function towerOfHanoi(n, fromRod, toRod, usingRod){
    if(n === 1){
        console.log(`Move disk 1 from ${fromRod} to ${toRod}`);
        return;
    }
    towerOfHanoi(n-1, fromRod, usingRod, toRod);
    console.log(`Move disk ${n} from ${fromRod} to ${toRod}`);

    towerOfHanoi(n-1, usingRod, toRod, fromRod);
}

towerOfHanoi(3, 'A', 'C', 'B');


// Big-O = O(2 ^ n)



/**
 * Must Learn
 * 
 * 1. Brute force
 * 2. Greedy
 * 3. Divide and conquer
 * 4. Dynamic Programming
 * 5. Back tracking
 */

/**
 * Next Steps
 * Tutorials: https://www.youtube.com/watch?v=poGEVboh9Rw&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=36
 * 
 * Solve more problems
 * 1. Finding the GCD using Euclidian algorithm
 * 2. Fining premutations and combindations of a list of numbers
 * 3. Finding the longest common substring in a given string
 * 4. Knapsack problem
 */