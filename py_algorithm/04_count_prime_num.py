"""
Tutorial: https://www.youtube.com/watch?v=FZTaNvbFcvM
Leetcode: https://leetcode.com/problems/count-primes/

204. Count Primes
Given an integer n, return the number of prime numbers that are strictly less than n.
Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7

Example 2:
    Input: n = 0
    Output: 0

Example 3:
    Input: n = 1
    Output: 0
"""

import math  # Importing the math module to use mathematical functions like sqrt.


# Brute force solution
class Solution:
    def __init__(self):
        self.n = None  # Initialize the class with a placeholder for the input number.

    def is_prime(self, n: int):
        # This method checks if a given number n is prime.
        for i in range(2, math.floor(math.sqrt(self.n)) + 1):
            # Loop from 2 to the square root of the number.
            if n % i == 0 and n != i:
                # If n is divisible by any number between 2 and sqrt(n), it's not a prime.
                return False  # Return False if n is not a prime number.
        return True  # Return True if n is a prime number.

    def countPrimes(self, n: int) -> int:
        self.n = n  # Store the input number in the class attribute.
        res = 0  # Initialize a counter to keep track of the number of primes.
        for x in range(2, n):
            # Loop through all numbers from 2 to n-1.
            res += int(self.is_prime(x))  # Increment the counter if x is prime.
        return res  # Return the total number of prime numbers found.


# Create an instance of the Solution class and call the countPrimes method with n = 12.
sol = Solution()
print("Brute force solution: ", sol.countPrimes(12))


# Sieve of Eratosthenes solution
class Solution2:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            # If n is less than or equal to 2, there are no prime numbers less than n.
            return 0

        # Initialize a list dp of size n with all True values.
        # dp[i] will be True if i is a prime number, otherwise False.
        dp = [True] * n
        dp[0] = False  # 0 is not a prime number.
        dp[1] = False  # 1 is not a prime number.

        for num in range(2, n):
            # Start from 2 and iterate up to n-1.
            if dp[num]:
                # If num is still marked as True, it's a prime number.
                for idx in range(num * 2, n, num):
                    # Mark all multiples of num as False, as they are not prime.
                    dp[idx] = False

        return sum(dp)  # The number of primes is the count of True values in dp.


# Create an instance of the Solution2 class and call the countPrimes method with n = 12.
sol2 = Solution2()
print("Sieve of Eratosthenes solution: ", sol2.countPrimes(12))
