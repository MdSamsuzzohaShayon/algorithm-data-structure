"""
Questions:
    What is the factorial of a number?
    How is the factorial of a number represented mathematically?
    What is the time complexity of the recursive approach to finding the factorial of a number?
    What are the differences between recursive and iterative methods for computing the factorial?
    Can you identify scenarios where calculating the factorial might be useful in real life?

Tasks:
    Basic:
        Write a Python function to compute the factorial of a number using recursion.
        Write a Python function to compute the factorial of a number using an iterative approach.
    Intermediate:
        Implement a memoized version of the factorial function to improve efficiency.
        Write a Python function to compute the factorial of a number using dynamic programming.
    Advanced:
        Create a Python program that computes the factorial of a very large number using the math module and handles large integers.
        Design a Python function that computes the factorial in parallel using multiprocessing to speed up the computation for large numbers.
"""

# Example 1: Basic Recursive Factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
print(factorial_recursive(5))  # Output: 120
# Explanation: This function uses recursion to compute the factorial. If n is 0 or 1, it returns 1. Otherwise, it recursively multiplies n by the factorial of n-1.

# Example 2: Basic Iterative Factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
print(factorial_iterative(5))  # Output: 120
# Explanation: This function uses an iterative approach to compute the factorial. It initializes a result variable to 1 and multiplies it by each number from 1 to n.

# Example 3: Memoized Factorial
def factorial_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 1
    else:
        memo[n] = n * factorial_memoized(n - 1, memo)
    return memo[n]

# Example usage:
print(factorial_memoized(5))  # Output: 120
# Explanation: This function uses memoization to store previously computed factorials in a dictionary to avoid redundant calculations.

# Example 4: Factorial with Dynamic Programming
def factorial_dp(n):
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i * dp[i - 1]
    return dp[n]

# Example usage:
print(factorial_dp(5))  # Output: 120
# Explanation: This function uses dynamic programming to store the results of subproblems in a list and builds up to the final result.
# Example 5: Factorial of Large Numbers
import math

def factorial_large(n):
    return math.factorial(n)

# Example usage:
print(factorial_large(100))  # Output: 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
# Explanation: This function uses the math module to compute the factorial, which is optimized for handling large integers.

# Example 6: Parallel Factorial Computation
from multiprocessing import Pool

def partial_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def factorial_parallel(n):
    num_processes = 4
    pool = Pool(processes=num_processes)
    step = n // num_processes
    ranges = [(i * step + 1, (i + 1) * step) for i in range(num_processes)]
    ranges[-1] = (ranges[-1][0], n)
    
    partial_results = pool.starmap(partial_factorial, ranges)
    result = 1
    for partial in partial_results:
        result *= partial
    
    return result

# Example usage:
print(factorial_parallel(20))  # Output: 2432902008176640000
# Explanation: This function uses multiprocessing to compute the factorial in parallel. It divides the range into chunks and computes partial factorials in parallel, then multiplies the partial results to get the final factorial.


