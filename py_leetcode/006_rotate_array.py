from typing import List

"""
Leetcode: https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
YouTube: https://www.youtube.com/watch?v=BHr381Guz3Y

189. Rotate Array
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]


Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105


Follow up:
    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array `nums` to the right by `k` steps in-place.

        The algorithm uses the reversal method to achieve the rotation.

        Steps:
        1. Normalize `k` to handle cases where `k` is greater than the length of the array. This is done using `k = k % len(nums)`.
        2. Reverse the entire array.
        3. Reverse the first `k` elements.
        4. Reverse the remaining `len(nums) - k` elements.

        The reversal method works as follows:
        - Reversing the entire array gives us a reversed version of the array.
        - Reversing the first `k` elements places the last `k` elements in their correct positions but still reversed.
        - Reversing the remaining elements places them in their correct positions.

        Time Complexity:
        - O(n): We perform three passes over the array (each reversal takes O(n) time).

        Space Complexity:
        - O(1): The algorithm uses constant extra space (for index variables and swapping).

        Parameters:
        - nums: List[int], the array to be rotated.
        - k: int, the number of steps to rotate the array.

        Returns:
        - None: The function modifies the array `nums` in-place.
        """

        # Normalize `k` to handle cases where `k` is greater than the length of the array
        k = k % len(nums)

        # Reverse the entire array
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # Reverse the first `k` elements
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # Reverse the remaining `len(nums) - k` elements
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


# Alternative Solution: Using a new array
# An alternative approach involves using an additional array to store the rotated result.
# This approach, while simpler, uses extra space.

class SolutionAlternative:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array `nums` to the right by `k` steps using an additional array.

        Steps:
        1. Normalize `k` to handle cases where `k` is greater than the length of the array. This is done using `k = k % len(nums)`.
        2. Create a new array `rotated` of the same length as `nums`.
        3. Place elements in their new positions according to the rotation.
        4. Copy the rotated array back to `nums`.

        Time Complexity:
        - O(n): We perform a pass to copy elements to the new array and another pass to copy back.

        Space Complexity:
        - O(n): We use an additional array of size `n` to store the result.

        Parameters:
        - nums: List[int], the array to be rotated.
        - k: int, the number of steps to rotate the array.

        Returns:
        - None: The function modifies the array `nums` in-place.
        """

        # Normalize `k` to handle cases where `k` is greater than the length of the array
        k = k % len(nums)

        # Create a new array for the rotated result
        rotated = [0] * len(nums)

        # Place elements in their new positions
        for i in range(len(nums)):
            rotated[(i + k) % len(nums)] = nums[i]

        # Copy the rotated array back to `nums`
        for i in range(len(nums)):
            nums[i] = rotated[i]