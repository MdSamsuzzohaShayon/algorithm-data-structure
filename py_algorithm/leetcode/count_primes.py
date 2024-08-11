import math

"""

Given an integer n, return the number of prime numbers that are strictly less than n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0

"""


class Solution:
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


sol = Solution()
print(sol.countPrimes(10))