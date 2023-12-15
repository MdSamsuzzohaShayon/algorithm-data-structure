"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
    Input: low = 3, high = 7
    Output: 3
    Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
    Input: low = 8, high = 10
    Output: 1
    Explanation: The odd numbers between 8 and 10 are [9].

Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105

LeetCode: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
YouTube Tutorial: https://www.youtube.com/watch?v=wrIWye928JQ&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=12
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        count = length // 2
        if length % 2 and low % 2:
            count += 1
        return count

# Big-O = O(1)
