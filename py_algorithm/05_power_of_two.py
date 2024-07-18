"""
Tutorial: https://www.youtube.com/watch?v=H2bjttEV4Vc
LeetCode: https://leetcode.com/problems/power-of-two/description/

231. Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:
    Input: n = 1
    Output: true
    Explanation: 20 = 1

Example 2:
    Input: n = 16
    Output: true
    Explanation: 24 = 16

Example 3:
    Input: n = 3
    Output: false


Constraints:
    -231 <= n <= 231 - 1


Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    """
    Method-1: Iterative Multiplication
    Explanation:
        If n is less than or equal to 0, it can't be a power of two.
        Start with x = 1 and repeatedly multiply x by 2.
        If at any point x equals n, then n is a power of two.
        If x exceeds n without being equal to n, then n is not a power of two.
    """
    def isPowerOfTwo1(self, n: int) -> bool:
        if n <= 0:
            return False
        x = 1
        while x <= n:
            if x == n:
                return True
            x *= 2

        return False
    # Big-O = Time complexity O(log n)
    # Big-O = Space complexity O(1)


    """
    Method 2: Optimized Iterative Multiplication
    Explanation:
        Start with x = 1 and repeatedly multiply x by 2.
        If x becomes equal to n, then n is a power of two.
        If x exceeds n, return false since n cannot be a power of two.
        This method skips the initial check for n <= 0 and assumes n is a positive integer.
    """
    def isPowerOfTwo2(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 2
        return x == n

    # Big-O = Time complexity O(log n)
    # Big-O = Space complexity O(1)

    """
    Method 3: Bitwise Operation
    Explanation:
        A power of two has exactly one bit set in its binary representation.
        For example, 2^3 = 8 is 1000 in binary.
        Subtracting 1 from a power of two flips all the bits after the only set bit. For 8 − 1 = 7 which is 0111.
        If n is a power of two, n & (n - 1) will be 0.
        This method checks if n is greater than 0 and if n & (n - 1) equals 0.
    """
    def isPowerOfTwo3(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
    # Big-O = Time complexity O(1)
    # Big-O = Space complexity O(1)

    """
    Method 4: Division by 2^30
    The maximum power of two that fits in a 32-bit signed integer is 2^30=1073741824.
    If n is a power of two, it must be a divisor of 2^30 .
    Check if 2^30 % == 0 .
    """
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and (2 ** 30 % n) == 0
        return n > 0 and ((1 << 30) % n) == 0
    # Big-O = Time complexity O(1)
    # Big-O = Space complexity O(1)


sol = Solution()
print(sol.isPowerOfTwo(1))
print(sol.isPowerOfTwo(16))
print(sol.isPowerOfTwo(3))



"""
Tutorial: https://www.youtube.com/watch?v=4cqHahxFTYw

Method-1: lease efficient
Keep dividing the number by 2
    16 = 16 / 2 = 8
    8 = 8 / 2 = 4
    4 = 4 / 2 = 2
    2 = 2 / 2 = 1
    
Method-2: Better than method 1 in efficiency
If the given number is divisible by two till we find 
"""