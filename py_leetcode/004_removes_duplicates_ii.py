from typing import List, Any

"""
Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
Youtube: https://www.youtube.com/watch?v=ycAq8iqh0TI&t=41s

80. Remove Duplicates from Sorted Array II
Medium
Topics
Companies
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

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

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize two pointers, l and r, both starting at the beginning of the array.
        # l is the slow pointer that will hold the position of the final valid array.
        # r is the fast pointer that scans through the entire array.
        l, r = 0, 0

        # Start iterating through the array with the right pointer `r`.
        while r < len(nums):
            # Initialize a count to 1 since we've encountered the first occurrence of nums[r].
            count = 1

            # Use the inner loop to check if the next elements are duplicates.
            # Keep moving the right pointer `r` as long as we find duplicate elements.
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1  # Move the right pointer to the next element.
                count += 1  # Increase the count of the current element's occurrence.

            # After counting the occurrences of nums[r], we need to copy it to the result array.
            # We only allow at most two occurrences of each element in the final array.
            # We use `min(2, count)` to ensure we don't add the element more than twice.
            for i in range(min(2, count)):
                nums[l] = nums[r]  # Place the element in the `l` position (valid portion of the array).
                l += 1  # Move the slow pointer `l` forward.

            # Move the right pointer `r` to the next new unique element.
            r += 1

        # After processing the entire array, the slow pointer `l` will be at the position
        # representing the length of the valid array (with at most two duplicates per element).
        return l  # Return the length of the modified array.

# Algorithm Used:
# The algorithm used here is a **two-pointer technique**, also known as the sliding window approach.
# The left pointer (`l`) is used to track the final length of the modified array, while the right pointer (`r`)
# is used to traverse the entire array, counting duplicates and adding at most two occurrences of each element to the valid portion.


# Time and Space Complexity:
# Time Complexity: O(n), where `n` is the length of the input array `nums`.
# - Each element in the array is processed once. Both `l` and `r` pointers traverse the array linearly, making the time complexity O(n).

# Space Complexity: O(1) (constant space).
# - The solution modifies the input array in place and uses only a few extra variables (`l`, `r`, `count`).
# - No additional space is allocated for another array.


# Optimized Version (More Efficient in Terms of Time and Space Complexity):
# The current solution is already optimal in terms of space complexity since it uses O(1) extra space.
# The time complexity is also optimal at O(n), as every element is visited at least once.
# However, a small refinement can be made by removing the `count` variable and simply tracking how many times an element
# has been added directly using a condition inside the loop.

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize two pointers
        l = 0  # Slow pointer (to modify the array in-place)

        # Iterate over the array using a fast pointer `r`
        for r in range(len(nums)):
            # Only place the element in the array if it's the first two occurrences
            # This is achieved by checking if `l < 2` or if the current element is greater than the element at position `l-2`.
            # The reason for the condition `l < 2` is to ensure that we can add the first two elements without any check.
            if l < 2 or nums[r] != nums[l - 2]:
                nums[l] = nums[r]  # Place the element in the valid portion
                l += 1  # Move the slow pointer forward to point to the next position for valid elements

        return l  # Return the length of the modified array

# Explanation of the optimization:
# - We removed the inner `while` loop and the `count` variable by using a condition that directly checks if we can place
#   the element at the slow pointer's position.
# - This is more concise and avoids the need for explicitly counting duplicates.
# - The time complexity remains O(n), as each element is still processed once.
# - The space complexity is still O(1), as the input array is modified in-place without additional space usage.


# Optimized Algorithm Analysis:

# Time Complexity: O(n)
# - The optimized version still has a time complexity of O(n) since each element is processed once.

# Space Complexity: O(1)
# - The space complexity remains constant at O(1) since we are modifying the array in place and not using any additional data structures.
