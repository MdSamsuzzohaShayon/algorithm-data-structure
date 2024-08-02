import numpy as np

"""
Questions
Basic:
    What is the Fibonacci sequence?
    Answer: The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It usually starts with 0 and 1. So, the sequence looks like this: 0, 1, 1, 2, 3, 5, 8, 13, and so on.
    How do you generate the nth Fibonacci number iteratively?
    How do you generate the first n Fibonacci numbers using a loop?

Intermediate:

    How do you generate the nth Fibonacci number using recursion?
    Answer: n-th Fibonacci number using recursion, you define the Fibonacci sequence with two base cases and a recursive case: Base Case F(0)=0 and 𝐹(1)=1. Recursive Case F(n)=F(n−1)+F(n−2)

    What are the time and space complexities of the recursive approach to generating Fibonacci numbers?
    Answer: Time Complexity: 𝑂(2^𝑛) The recursive approach has exponential time complexity because it makes multiple recursive calls for each Fibonacci number. Each call generates two more calls,
    leading to a binary tree of calls with an exponential number of nodes. Space Complexity: 𝑂(𝑛) The space complexity is 𝑂(𝑛) due to the call stack. In the worst case, the depth of the recursive
    call stack can be as large as 𝑛, where n is the input number.

    How can you use memoization to optimize the recursive Fibonacci function?
    Answer: Memoization can significantly optimize a recursive Fibonacci function by storing the results of previously computed Fibonacci numbers, thereby avoiding redundant calculations.
    Create a Cache: Use a data structure (like a dictionary) to store the results of Fibonacci calculations. Check the Cache: Before performing a calculation, check if the result is already in the
    cache. Store the Result: After calculating the result, store it in the cache for future use.

Advanced:
    How do you generate the nth Fibonacci number using matrix exponentiation?
    
    Answer: The time complexity of generating the n-th Fibonacci number using matrix exponentiation is O(log n)
    What is the time complexity of generating the nth Fibonacci number using matrix exponentiation?
    
    How can you generate Fibonacci numbers using dynamic programming?
    Answer: Generating Fibonacci numbers using dynamic programming involves storing previously computed values to avoid redundant calculations, which significantly improves efficiency. 
    The dynamic programming approach can be implemented in two main ways: tabulation (bottom-up approach) and memoization (top-down approach). Tabulation (Bottom-Up Approach) This method builds the 
    solution iteratively from the base cases up to the desired n-th Fibonacci number.

"""
# Write code

"""
Tasks
Basic:
    Write a function to generate the first n Fibonacci numbers iteratively.
    Write a function to print the nth Fibonacci number iteratively.
    Write a program to display the Fibonacci sequence up to a given number of terms.
    
Intermediate:
    Write a recursive function to generate the nth Fibonacci number.
    Write a function to generate the first n Fibonacci numbers using recursion.
    Implement memoization to optimize the recursive Fibonacci function.

Advanced:
    Implement a function to generate the nth Fibonacci number using matrix exponentiation.
    Write a function to generate the nth Fibonacci number using dynamic programming.
    Compare the performance of iterative, recursive, and matrix exponentiation methods for generating the nth Fibonacci number.
"""


# Basic Example: Generating the First n Fibonacci Numbers Iteratively

def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


# Example usage
print(fibonacci_iterative(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Intermediate Example: Generating the nth Fibonacci Number Using Recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Example usage
print(fibonacci_recursive(10))  # Output: 55


# Intermediate Example with Memoization
def fibonacci_memoization(n, memo={}):
    # Optimization by memoization
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


# Example usage
print(fibonacci_memoization(10))  # Output: 55


# Advanced Example: Generating the nth Fibonacci Number Using Matrix Exponentiation


def matrix_mult(A, B):
    return np.dot(A, B)


def matrix_pow(matrix, power):
    result = np.identity(len(matrix), dtype=int)
    base = matrix
    while power:
        if power % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        power //= 2
    return result


def fibonacci_matrix_exponentiation(n):
    if n <= 1:
        return n
    F = np.array([[1, 1],
                  [1, 0]], dtype=int)
    result = matrix_pow(F, n - 1)
    return result[0][0]


# Example usage
print(fibonacci_matrix_exponentiation(10))  # Output: 55

"""
Explanations
Basic Example: The function fibonacci_iterative generates the first n Fibonacci numbers using an iterative approach.
Intermediate Example: The function fibonacci_recursive demonstrates how to generate the nth Fibonacci number using recursion.
Intermediate Example with Memoization: The function fibonacci_memoization optimizes the recursive approach by storing previously computed values to avoid redundant calculations.
Advanced Example: The function fibonacci_matrix_exponentiation uses matrix exponentiation to generate the nth Fibonacci number efficiently, demonstrating an advanced method with a better time complexity compared to the simple recursive approach.
"""

# https://www.youtube.com/watch?v=eMXNWcbw75E
# Matrix Exponentiation + Fibonacci in log(N)
