/**
 * Tutorial-1: https://youtu.be/HzeK7g8cD0Y
 * Tutorial-2: https://youtu.be/lfQvPHGtu6Q
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


