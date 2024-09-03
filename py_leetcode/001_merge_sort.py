from typing import List

"""
Youtube-1: https://www.youtube.com/watch?v=0-KuWOcHZuk
Leetcode: https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and 
should be ignored. nums2 has a length of n.

 

Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].
    
Example 3:
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 
Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109
 
Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""


# The goal is to merge the two arrays in O(m + n) time complexity and store the result in-place in nums1.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        This function modifies nums1 in-place, merging the elements from nums2 into nums1
        in non-decreasing order.

        Approach:
        - We use a two-pointer technique starting from the end of nums1 and nums2 to merge the arrays in reverse.
        - We start from the back of nums1 and nums2 since nums1 has extra space at the end.
        - We compare elements from the end and insert the larger of the two elements at the correct position.

        Parameters:
        - nums1: List[int], first sorted array with extra space at the end to accommodate nums2.
        - m: int, number of valid elements in nums1.
        - nums2: List[int], second sorted array.
        - n: int, number of elements in nums2.
        """

        # Initialize pointers x and y for nums1 and nums2 respectively.
        # x points to the last valid element in nums1, and y points to the last element in nums2.
        x, y = m - 1, n - 1

        # Loop over the combined size of nums1 and nums2 backwards (m + n - 1 to 0).
        # z is the pointer that starts at the last index of nums1 and decrements to fill it in reverse.
        for z in range(m + n - 1, -1, -1):  # Looping backwards from the end of nums1.

            # If all elements from nums1 are placed but nums2 still has elements,
            # we place the remaining elements of nums2 into nums1.
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1  # Move the pointer in nums2 backwards.

            # If all elements from nums2 have been placed, break out of the loop as the array is sorted.
            elif y < 0:
                break  # No need to do anything since nums1 is already sorted.

            # Compare the elements from nums1 and nums2 that have not been placed yet.
            # If nums1's current element is greater, place it at the end and move the pointer.
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]  # Place nums1's element in the correct position.
                x -= 1  # Move the pointer in nums1 backwards.

            # Otherwise, place nums2's element at the end and move the pointer in nums2.
            else:
                nums1[z] = nums2[y]  # Place nums2's element in the correct position.
                y -= 1  # Move the pointer in nums2 backwards.


# Time Complexity: O(m + n)
# - We iterate over the combined length of nums1 and nums2, making the time complexity O(m + n).
# - Each comparison between the elements from nums1 and nums2 is done in constant time.

# Space Complexity: O(1)
# - The function modifies nums1 in place without using any additional space, so the space complexity is O(1).

# More efficient approach?
# - The current solution is already optimal for this problem. It achieves O(m + n) time complexity with
#   O(1) space complexity, which is the most efficient we can get for merging two sorted arrays in place.


# Example usage of the solution:
sol = Solution()
sol.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)

# Expected Output: Nums1 After: [1, 2, 2, 3, 5, 6]
