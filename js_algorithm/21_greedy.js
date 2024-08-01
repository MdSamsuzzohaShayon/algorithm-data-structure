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