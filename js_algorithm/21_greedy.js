/**
 * Tutorial-1: https://youtu.be/HzeK7g8cD0Y
 * Tutorial-2: https://youtu.be/lfQvPHGtu6Q
 * Tutorial-3: https://youtu.be/3H2G3KuEiRU
 * 
 * 
 * An algorithm paradigram that follows the problem solving approach of making the locally optimal choice at each stage with the hope of finding a global optimum.
 * 
 * Pros: simple, easy to implement, run fast
 * Cons: Very often they do not provide a globally optimum solution
 * 
 * Problems on which greedy approach work has two properties
 * 1. Greedy - choice property: A global optimum can be arrived at by selecting a local optimum.
 * 2. Optimal substructure: An optimal solution to the problem contains an optimal solution to sub problems
 * 
 * Applications
 *      1. Activity selection problem 
 *      2. Huffman coding
 *      3. Job sequence problem
 *      4. Fractional knapsack problem
 *      5. Prim's minimum spanning tree
 * 
 * 
 * Example-1: 
 *      There is an array of integers [3, 4, -1, 2, -3, 0] and n = 4
 *      Find the n number in this array ity equal the leargest sum
 *      Select the leargest number in every single step until we select the n number
 * 
 *      Answer: So we can select 4 + 3 + 2 + 1 = 10 is the leargest sum
 *      Here the leargest number we can create is 6 by select 4 numbers
 * 
 * Knapsack problem
 * 
 *      Capacity = 25 means we can store 25 items in our backpack/weight
 *      
 *      Item     Size    Value      Value/Size
 *      =========================================
 *       0        22       19       0.8636
 *       1        10       9        0.9
 *       2        10       9        1
 *       3        7        6        0.857
 *      
 *      Fill the back pack with as much value as possible without going over it's capacity
 * 
 */

/**
 * Example-1: Maximum Sum Subsequence
 * Given an array of integers and an integer n, find the n numbers in the array that sum to the largest possible value.
 * 
 * Array: [3, 4, -1, 2, -3, 0]
 * n: 4
 * 
 * Find the n largest numbers in the array and return their sum.
 * @param {number[]} arr - The array of integers.
 * @param {number} n - The number of elements to sum.
 * @returns {number} - The largest sum of n numbers.
 */
function maxSum(arr, n) {
    // Sort the array in descending order
    arr.sort((a, b) => b - a);

    // Select the first n elements and calculate their sum
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += arr[i];
    }

    return sum;
}

// Example usage:
console.log(maxSum([3, 4, -1, 2, -3, 0], 4)); // Output: 8 (4 + 3 + 2 + -1)


/**
 * Example-2: Fractional Knapsack Problem
 * Given items with sizes and values, fill a knapsack of a given capacity to maximize the total value.
 * 
 * Capacity: 25
 * 
 * Solve the fractional knapsack problem.
 * @param {Object[]} items - Array of items with size and value.
 * @param {number} capacity - The total capacity of the knapsack.
 * @returns {number} - The maximum value that fits in the knapsack.
 */
function fractionalKnapsack(items, capacity) {
    // Calculate value-to-weight ratio for each item
    items.forEach(item => item.ratio = item.value / item.size);

    // Sort items by their value-to-weight ratio in descending order
    items.sort((a, b) => b.ratio - a.ratio);

    let totalValue = 0;

    // Select items to maximize total value without exceeding capacity
    for (let item of items) {
        if (capacity >= item.size) {
            // If the knapsack can carry the whole item, add its full value
            capacity -= item.size;
            totalValue += item.value;
        } else {
            // If the knapsack can't carry the whole item, add fractional value
            totalValue += item.value * (capacity / item.size);
            break;
        }
    }

    return totalValue;
}

// Example usage:
const items = [
    { size: 22, value: 19 },
    { size: 10, value: 9 },
    { size: 10, value: 9 },
    { size: 7, value: 6 }
];
console.log(fractionalKnapsack(items, 25)); // Output: 24.8


/**
 * Example-3: Activity Selection Problem
 * Select the maximum number of activities that don't overlap.
 *
 * Activities: [{start: 1, end: 3}, {start: 2, end: 5}, {start: 4, end: 6}, {start: 6, end: 7}, {start: 5, end: 8}, {start: 8, end: 9}]
 * 
 * 
 * Select the maximum number of non-overlapping activities.
 * @param {Object[]} activities - Array of activities with start and end times.
 * @returns {Object[]} - The selected activities.
 */
function activitySelection(activities) {
    // Sort activities by their end times
    activities.sort((a, b) => a.end - b.end);

    let selectedActivities = [];
    let lastEndTime = 0;

    // Select activities that don't overlap
    for (let activity of activities) {
        if (activity.start >= lastEndTime) {
            selectedActivities.push(activity);
            lastEndTime = activity.end;
        }
    }

    return selectedActivities;
}

// Example usage:
const activities = [
    { start: 1, end: 3 },
    { start: 2, end: 5 },
    { start: 4, end: 6 },
    { start: 6, end: 7 },
    { start: 5, end: 8 },
    { start: 8, end: 9 }
];
console.log(activitySelection(activities)); // Output: [{start: 1, end: 3}, {start: 4, end: 6}, {start: 6, end: 7}, {start: 8, end: 9}]


console.log("===== Break =====");
/**
 * Choose the best possible solution
 * If feasible, add it to the solution set
 * If not, reject it and do not consider it again
 * Keep repeating, until we reach the end
 */


/**

Greedy Algorithm
A greedy algorithm is a simple, intuitive algorithmic technique that is used in optimization problems. The algorithm
makes the best possible choice at each step with the hope of finding the global optimum.
Key Characteristics
Greedy Choice Property: A global optimum can be arrived at by selecting a local optimum.
Optimal Substructure: A problem has optimal substructure if an optimal solution to the problem contains optimal
solutions to the sub-problems.
Real-Life Example
Imagine you are at a candy store with a limited amount of money. You want to buy as many candies as possible. You
will likely choose the cheapest candies first to maximize the number you can buy. This is a greedy approach because
at each step, you make the choice that seems the best at that moment.
Coding Example: Coin Change Problem
Given a set of coin denominations and a target amount, find the minimum number of coins needed to make the target
amount. This problem assumes that you have an infinite supply of coins for each denomination.
JavaScript Implementation
*/

// Function to find the minimum number of coins
function minCoins(coins, amount) {
    // Sort coins in descending order
    coins.sort((a, b) => b - a);
    
    let count = 0;
    
    for (let coin of coins) {
        if (amount === 0) break;
        if (coin <= amount) {
            // Use as many coins of this denomination as possible
            let numCoins = Math.floor(amount / coin);
            amount -= numCoins * coin;
            count += numCoins;
        }
    }
    
    // If the amount is not zero, it means we cannot give the exact amount with the given denominations
    return amount === 0 ? count : -1;
    }

// Example usage
const coins = [1, 2, 5, 10];
const amount = 27;
console.log(`Minimum coins needed: ${minCoins(coins, amount)}`); // Output: 4 (10 + 10 + 5 + 2)

/**

Another Example: Activity Selection Problem
Given a set of activities with their start and end times, select the maximum number of activities that can be
performed by a single person, assuming that a person can only work on a single activity at a time.
JavaScript Implementation
*/
// Function to select the maximum number of activities
function activitySelection(activities) {
    // Sort activities based on their end time
    activities.sort((a, b) => a.end - b.end);
    let selectedActivities = [];
    let lastEndTime = 0;

    for (let activity of activities) {
        if (activity.start >= lastEndTime) {
            // Select this activity
            selectedActivities.push(activity);
            lastEndTime = activity.end;
        }
    }

    return selectedActivities;
}

// Example usage
const activities_two = [
    { start: 1, end: 3 },
    { start: 2, end: 5 },
    { start: 4, end: 7 },
    { start: 1, end: 8 },
    { start: 5, end: 9 },
    { start: 8, end: 10 }
];
console.log("Selected activities:", activitySelection(activities_two));

/**

Conclusion
Greedy algorithms are useful for solving optimization problems where making local optimal choices at each step
leads to a global optimal solution. However, they do not always produce the optimal solution for every problem,
so it's important to understand the problem's properties before applying a greedy algorithm.
In summary, greedy algorithms:
Are easy to implement and understand.
Provide a good starting point for optimization problems.
May not always produce the optimal solution but can offer a quick approximation.
*/


