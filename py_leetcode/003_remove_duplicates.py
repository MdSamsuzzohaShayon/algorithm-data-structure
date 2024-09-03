from typing import List, Any

"""
Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
YouTube: https://www.youtube.com/watch?v=DEJAZBq0FDA

26. Remove Duplicates from Sorted Array
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
    
    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    
    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.
    Custom Judge:
    
    The judge will test your solution with the following code:
    
    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length
    
    int k = removeDuplicates(nums); // Calls your implementation
    
    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.

 

Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        This function removes duplicates from the sorted array `nums` in-place.
        It modifies the array such that the first `k` elements contain the unique values in their original order.
        The remaining elements in `nums` can be ignored.

        Approach:
        - Use two pointers technique: `l` (left) will keep track of the position to place the next unique element.
        - `r` (right) will iterate through the array, comparing the current element `nums[r]` with the previous element `nums[r-1]`.
        - If the current element is different from the previous one, it is unique, and we move it to the `l` position.
        - The process continues until we traverse the entire array.

        Parameters:
        - nums: List[int], the input sorted array from which duplicates will be removed.

        Returns:
        - l: int, the number of unique elements in the array (i.e., the length of the unique portion of the array).
        """

        # Start `l` (left pointer) at index 1 since the first element is always unique by default.
        l = 1

        # Loop through the array starting from index 1 using the `r` (right pointer).
        # We start from index 1 because we compare `nums[r]` with `nums[r-1]`, so we need to start comparison from the second element.
        for r in range(1, len(nums)):

            # If the current element `nums[r]` is not equal to the previous element `nums[r-1]`,
            # it means `nums[r]` is a unique element.
            if nums[r] != nums[r - 1]:
                # Place the unique element `nums[r]` at index `l`, and then increment `l`.
                # This effectively moves the unique elements to the front of the array.
                nums[l] = nums[r]
                l += 1  # Increment `l` to move to the next position for the next unique element.

        # After the loop, `l` will be the number of unique elements in the array.
        # The first `l` elements of `nums` will contain the unique elements in their original order.
        return l

# Time Complexity: O(n)
# - We are iterating through the array `nums` once, where `n` is the length of the array.
# - Each element is compared once and, if unique, placed in the `l` index, which results in linear time complexity, O(n).

# Space Complexity: O(1)
# - The function modifies the input array `nums` in-place without using any extra space.
# - We are only using two pointers (`l` and `r`), which are independent of the input size, making the space complexity O(1).

# Explanation of Efficiency:
# - This solution is already optimal. The two-pointer technique ensures that we are processing the array in a single pass.
# - No additional space is used, and the algorithm runs in linear time, which is the best time complexity possible for this problem.
