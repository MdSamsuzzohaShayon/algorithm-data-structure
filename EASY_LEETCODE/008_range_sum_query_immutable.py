"""
Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example-1:
    Input
        ["NumArray", "sumRange", "sumRange", "sumRange"]
        [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    Output
        [null, 1, -1, -3]

LeetCode: https://leetcode.com/problems/range-sum-query-immutable/
YouTube Tutorial: https://www.youtube.com/watch?v=2pndAmo_sMA&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=7
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0
        for n in nums:
            curr += n
            self.prefix.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left-1] if left > 0 else 0
        return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)