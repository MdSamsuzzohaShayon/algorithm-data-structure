# https://www.youtube.com/watch?v=FggXDrgeI20&t=20s

"""
Leetcode

Fibonacci Number
The fibonacci numbers, commonly denoted F(n) from a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones,
 starting from 0 and 1 that is:
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) , for n > 1

Given n, calculate (n)

Example 1:
    Input n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1

Example 2:
    Input n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2

Example 3:
    Input n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3

"""


class Solution:
    def fib(self, n: int) -> int:
        # Recursive solution
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 2) + self.fib(n - 1)


sol = Solution()
print(sol.fib(2))
print(sol.fib(3))
print(sol.fib(4))

"""
Top down dynamic programming
Memoization / Cache / Memo
"""


class Solution2:
    def fib(self, n: int) -> int:
        # Recursive solution
        memo = {0: 0, 1: 1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x - 1) + f(x - 2)
                return memo[x]

        return f(n)


sol2 = Solution2()
print("Top-down solution: ", sol2.fib(6))
# Big-O of Time Complexity: O(n)
# Big-O of Space Complexity: O(n)


"""
Optimization because it's avoid recursion (Preferred)
Bottom up - tabulation
"""


class Solution3:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]


sol3 = Solution3()
print("Bottom up solution: ", sol3.fib(6))


# Big-O of Time Complexity: O(n)
# Big-O of Space Complexity: O(n)


class Solution4:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 0
        curr = 1
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr


sol4 = Solution4()
print("Bottom up solution: ", sol4.fib(6))


# Big-O of Time Complexity: O(n)
# Big-O of Space Complexity: O(1)


class Solution5:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + (5 ** 0.5)) / 2
        return int(round((golden_ratio ** n) / (5 ** 0.5)))


sol5 = Solution5()
print("Golden ratio: ", sol5.fib(6))
