# Algorithm
 - [Tutorials](https://www.youtube.com/watch?v=8hly31xKli0&t=23s)
 - A set of steps or instructions for completing a task.
 - Need clearly defined problem statement, input and output
 - The steps also tb be distinct (should not able to break it down to further subtask)
 - The algorithm should produce a result
 - Algorithm should actually complete and not take an infinite amount of time
 - Search algorithm
 - The steps in the algorithm need to be in a very specific order. 

    

### Guideline

 - Breakdown the problem with any possible number of smaller problem
 - Problem: clearly defined input satisfying any pre-condition, and a clearly defined output 
 - **Correctness**: Part of any possible input the algorithm should always terminate or end. If the condition is not true then our algorithm is incorrect.
 - **Efficiency**: It helps to solve problem faster, and deliver better user experience. Measuring efficiency we always use worse case scenario as the benchmark because it can never perform worse than the worst case.
 - Two Major Efficiency: Time and space - Good algorithm need to balance between these two measures to be useful.
   - Time complexity: Measure how long it takes the algorithm to run.
   - Space complexity: it deals with the amount of memory taken up on the computer.

### Search algorithm
 - Run against lsts containing all sorts of data. It is not always just range of values containing numbers. In real use case of binary search  the algorithm would not return the target value because we already know that. Instead what is returns is the position in the list that the target occupies.
   
### Linear Search 
 - Input is list of value and output is the target value or position of target value.
    1. Start at beginning
    2. Move sequentially
    3. Compare current value to target
    4. React end of list

### Binary Search

 - Input is sorted list of values and output is the position in the list of the target value we are searching. Or some sort of values indicates that the target does not exist in the list.
 - Example: Search 20 in list of 100 like [1, 2,3,4 so on]. Target is 5 here. 
    - Step-1: First check the middle position element 10 check if target element match or not.
    - Step-2: If middle element doesn't match check target is greater or less than middle element.
    - Step-3: If target element is less than middle element check in middle of beginning to middle element. in this case it is from 1 to 10 and check with muddle of that which is 5.
    - Step-4: Do divide with 2 and comparing with middle element until we get our target value.
    - Step-5: If any of them doesn't match with target then return a exception with **Target value doesn't exist** 

 - Growth rate: different algorithm grow at different rate abd by evaluating growth rate we get a much better picture of their performance because we know how the algorithm will hold up as n grows larger.

### Big O
 
 - Definition of the complexity of an algorithm as a function of the size. Complexity is relative
 - Big O is a notation used to describe complexity. Notation simplifies everything into a single variable.
 - Order of magnitude of complexity - O(n). A function  of the size. Big O measures complexity as the input size grows. Big O refer to as the upper bound of the algorithm. Here n  means numbers of operations.
 - Big O is a useful notation for understanding both time and space complexity but only when comparing amongst algorithms that solve the same problem.
 - A function of the size: Big O measure the complexity as the input size grows because it's not important to understand how an algorithm performs in a single dataset but in all possible data sets.
 - Also, big O refer to upper bound of the algorithm. big O measure how the algorithm performs in the worst case scenario.
 - linear search big O = O(n), Binary search big o = O(log n)
 - Constant time: input size doesn't matter. regardless of the size of n since this takes the same amount of time in any given case then runtime is constant time it doesn't change. In big O notation it looks like O(1)
 - Exponent 2^3=8 and inverse of exponent called logarithm log _2 8 = 3
 - **Logarithmic** : or sub-linear runtimes are preferred to linear because they are more efficient but in practice linear search has its own search of advantages
 - **Quadratic runtime** : (square or to the power): For any given value of n carry out n squared number of operation. ex- n = 4, n^2 = 16, 4 x 4 grid = O(n^2)
 - **Cubic runtime** : n^3 . This are as common as quadratic runtime.
 - **Quasi-linear** : Quasi-linear runtime are written out as big o of n times log n. ex: O(n log n). For every value of n need to execute a log n number of operations hence the runtime of n times log n.
 - **Polynomial Runtime** : An algorithm is considered to have a polynomial runtime if for a given value of n its worst case runtime is in the form of n raised to the k power where k just means some value. ex: k = 2, O(n^k)
 - Algorithm with an upper bound or a runtime with a big O value that is polynomial are considered efficient algorithms. 
 - **Exponential runtime** : N increases slidly, number of operation increases exponentially. O(x^n). The range of value we have to go to is 00 to 99 ant this can be generalized as 10^2. Searching though each individual until stumnle to the right one is a strategy call brute force and brute force algorithm have exponential runtime.
   1. This algorithm is insufficiant
   2. Number of operation increases segnificantly, 
   3. As n increases number of opertions increases exponentially to a point where it's unsolvable in a realistic amount of time.

 - **Factorial runtime** : n! = n(n-1)(n-2)...(2)(1) . For example foctorial of 3 is 3! = 3 x 2 x 1 = 6, factorial of 4 is !4 = 4 x 3 x 2 x 1. In solving the traveling salesman problem the most efficient algorithm is factorial runtime of a combinatorial runtime.


### Data Structures
 - Data structure is a way of storing data in programming. It's not just collection of value and formant they are stored in but the relationship between the values in the collection as well as the operations applied on the data stored in the structure.
 - Data structure is a data storage format. it is collection of values and the format they are stored in, the relationships between the values in the collection as well as the operations applied on the data stored in the structure.
 - **Array** - can be used to represent a collection of values where each value is referanced using an index or a key.Arrays are also used in building block to create even more custom data types and structures. 
   - Arrays is stored in blocks of memory that are right beside each other with no gap
   - Arrays can be either hmogeneous containing same type of value(Python, JavaScript) or heterogeneous where any kind of value can be mixed(C, Swift, Java)
 - Advantages of contiguous memory: since the values are stored beside each other accessing the values happens in almost constant time so this is a characteristic we want. The way python gets around this is by allocating contiguous memory and storing in it not the value we want to store but a reference or a pointer to the value that is stored somewhere else in memory
 - **Common operations to execute on an array**: All data structure expected to cary out 4 kinds of operations at minimum
   1. Access and read values
   2. Search for an arbitrary values
   3. Insert values at any point into the structure
   4. delete values in the structure

 - **String** - Text are represented as string type and under the hood strings are just a bunch of charecters stored in a particular order in an array

 - **Build Data Structure** - Each data structure solves a particular problem. Arrays are particularly goot at accessing, reading values happen in constant time but Arrays are pretty bar at inserting and deleting both of which run in linear time. Linkedlist on the other hand are somewhat better at this although there are some caveats and if we are trying to solve a problem involves far more inserts and deletes than accessing a linkedlist can be a better tool than array. 
 - **Linkedlist** - Linkedlist is a linear data structure where each element in the list is contained in a separate object called a node, a node models two pieces of information an individual item of the data we want to and a reference to the next node in the list
   - First node is called the head of the list
   - Last node is called tail of the list and tail does not point to anything(Self referential objects)
   - Every node other than tail points to the next 
   - The list only maintains a reference to the head although in some impementation is keeps a reference to the tail as well
   - Singly linkedlist where each node stores a reference to the next node
   - Doubly linked list where each node stores a reference to both the node before and after
   - Linked is really useful structure to build for learning purposes because they are relatively simple and are a good place to start to introduce the kinds of operations we need to implement for various data structure
 
 - **Sort Algorithm** - merge [03:03:00]
 - Goal is to get an array sorted in ascending order
 - Merge sort work like binary sort by splitting up the problem into sub problems 
   1. Split the array into two smaller array or sub array
   2. on first pass Unlike binary search in merge search one the sub array will not be discarded
   3. on second pass each of those sub arrays into further smaller evenly sized arrays
   4. Keep doing this until we are down to single element(one element in an array) arrays
 - Merge sort algorithm works backwards repeatedly merging the single element array and sorting them at the same time
 - Since we start at the bottom by merging to single element arrays, we only need to make a single comparison to sort the result 
 - By starting the smaller array that are sorted as they grow merge sort has to execute fewer sort operations than if it sorted the entire array at once
 - Solving a problem like this by recursively breaking down the problem into subpart until it is easily solved is an algorithmic strategy known as *divide and conquer*

03:52:00



