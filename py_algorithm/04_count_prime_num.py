"""
Tutorial: https://www.youtube.com/watch?v=FZTaNvbFcvM
Leetcode: 204. Count Primes
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

import math


# Brute force solution
class Solution:
    def __init__(self):
        self.n = None

    def is_prime(self, n: int):
        for i in range(2, math.floor(math.sqrt(self.n)) + 1):
            if n % 1 == 0 and n != i:
                return False

    def countPrimes(self, n: int) -> int:
        self.n = n
        res = 0
        for x in range(2, n):
            res += int(self.is_prime(x))
        return res


sol = Solution()
print("Brute force solution: ", sol.countPrimes(12))


# Sieve of Eratosthenes
class Solution2:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        dp = [True] * n
        dp[0] = False
        dp[1] = False

        for num in range(2, n):
            if dp[num]:
                for idx in range(num * 2, n, num):
                    dp[idx] = False

        return sum(dp)


sol2 = Solution2()
print("Sieve of Eratosthenes solution: ", sol2.countPrimes(12))
