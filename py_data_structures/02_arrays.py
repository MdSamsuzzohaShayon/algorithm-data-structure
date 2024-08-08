from typing import List

"""
YouTube: https://youtu.be/BHr381Guz3Y
Leetcode: https://leetcode.com/problems/rotate-array/description/

189. Rotate Array
Hint:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 step to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation:
    rotate 1 step to the right: [99,-1,-100,3]
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
        Rotate the array nums to the right by k steps in-place.

        Parameters:
        nums (List[int]): The list of integers to be rotated.
        k (int): The number of steps to rotate the array.

        Returns:
        None: The function modifies the array in-place.
        """

        # Step 1: Normalize k to avoid unnecessary rotations
        k = k % len(nums)  # Handle cases where k is greater than the length of the array

        # Step 2: Reverse the entire array
        left, right = 0, len(nums) - 1
        while left < right:
            # Swap elements at left and right indices
            nums[left], nums[right] = nums[right], nums[left]
            # Move towards the center
            left, right = left + 1, right - 1

        # Step 3: Reverse the first k elements
        left, right = 0, k - 1
        while left < right:
            # Swap elements at left and right indices within the first k elements
            nums[left], nums[right] = nums[right], nums[left]
            # Move towards the center of this segment
            left, right = left + 1, right - 1

        # Step 4: Reverse the remaining elements from k to the end
        left, right = k, len(nums) - 1
        while left < right:
            # Swap elements at left and right indices within the remaining segment
            nums[left], nums[right] = nums[right], nums[left]
            # Move towards the center of this segment
            left, right = left + 1, right - 1

        # Time complexity for reversing the remaining elements: O(n - k)

        # Total time complexity: O(n) because O(k) and O(n - k) together cover all n elements

        # Space complexity:
        # We use a constant amount of extra space for variables (left, right, k)
        # No extra space is used proportional to the input size
        # Therefore, space complexity: O(1)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    solution.rotate(nums1, k1)
    print(nums1)  # Output should be [5, 6, 7, 1, 2, 3, 4]

    # Test Case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    solution.rotate(nums2, k2)
    print(nums2)  # Output should be [3, 99, -1, -100]

    # Test Case 3: Edge case with k = 0
    nums3 = [1, 2, 3, 4, 5]
    k3 = 0
    solution.rotate(nums3, k3)
    print(nums3)  # Output should be [1, 2, 3, 4, 5]

    # Test Case 4: Edge case where k is greater than the length of the array
    nums4 = [1, 2, 3, 4, 5]
    k4 = 7
    solution.rotate(nums4, k4)
    print(nums4)  # Output should be [4, 5, 1, 2, 3]
