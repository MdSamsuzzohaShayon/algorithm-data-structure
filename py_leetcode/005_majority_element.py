from typing import List

"""
Leetcode: https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
Youtube: https://youtu.be/7pnhv842keE

169. Majority Element
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:
    Input: nums = [3,2,3]
    Output: 3

Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2


Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


class Solution:

    """
    Easy solution:

    def majorityElement(self, nums: List[int]) -> int:
        count  = {}
        res, maxCount = 0, 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res
    """



    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element in the array using the Boyer-Moore Voting Algorithm.

        Algorithm Explanation:
        - The Boyer-Moore Voting Algorithm helps find the majority element in linear time and constant space.
        - We use a variable `res` to keep track of the current candidate for majority element.
        - We use a `count` variable to keep track of the balance between the candidate and other elements.

        Steps:
        1. Initialize `res` to 0 and `count` to 0.
        2. Iterate through each element `n` in the array `nums`.
        3. If `count` is 0, set `res` to the current element `n`. This indicates a new candidate for majority element.
        4. If the current element `n` is the same as `res`, increment `count`. Otherwise, decrement `count`.
        5. After the loop, `res` will be the majority element.

        Time Complexity:
        - O(n): We traverse the array once, where `n` is the length of the array.

        Space Complexity:
        - O(1): We use only a constant amount of extra space (variables `res` and `count`).

        Parameters:
        - nums: List[int], the input array from which to find the majority element.

        Returns:
        - int: The majority element in the array.
        """

        # Initialize `res` to keep track of the current majority candidate and `count` to maintain the count balance.
        res, count = 0, 0

        # Iterate through each element in the array
        for n in nums:
            # If the count is zero, assign the current element as the new candidate
            if count == 0:
                res = n
            # Update the count: increment if the current element matches the candidate, otherwise decrement
            count += (1 if n == res else -1)

        # Return the majority element found
        return res


# Time Complexity: O(n)
# - We perform a single pass over the array to determine the majority element.

# Space Complexity: O(1)
# - The algorithm uses a constant amount of space for `res` and `count`, regardless of the input size.

# Alternative Solution:
# An alternative approach involves using a hash map to count occurrences of each element.
# However, this would use O(n) space which is not optimal for the given problem constraints.
# The Boyer-Moore Voting Algorithm is the most efficient solution in terms of both time and space complexity.

sol = Solution()
print("Majority Element: ",sol.majorityElement([2,2,1,1,1,2,2]))