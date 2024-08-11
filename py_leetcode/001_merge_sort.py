from typing import List

"""
Youtube-1: https://www.youtube.com/watch?v=0-KuWOcHZuk
Leetcode: https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

88. Merge Sorted Array
Easy
Hint
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


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        This function merges nums2 into nums1 in-place.
        It modifies nums1 directly, so no need to return anything.
        """

        # Print the initial state of nums1
        print("Nums1 Before: ", nums1)

        # Initialize two pointers x and y
        # x points to the last element in the first `m` elements of nums1
        # y points to the last element in nums2
        x, y = m - 1, n - 1

        # We will also have a pointer z starting from the end of nums1 (which is m + n - 1)
        # This pointer z will be used to fill nums1 from the end.
        for z in range(m + n - 1, -1, -1):  # Looping backwards from the end of nums1

            # If there are no more elements to consider in nums1 (x < 0),
            # take elements from nums2 directly and put them in nums1.
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1  # Move the y pointer to the left (to the next element in nums2)

            # If there are no more elements to consider in nums2 (y < 0),
            # we can stop because nums1 is already sorted, and no more action is needed.
            elif y < 0:
                break

            # If the current element in nums1 (nums1[x]) is greater than the current element in nums2 (nums2[y]),
            # move nums1[x] to the current position z, and move x pointer to the left.
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1

            # If nums2[y] is greater than or equal to nums1[x],
            # place nums2[y] at the current position z, and move y pointer to the left.
            else:
                nums1[z] = nums2[y]
                y -= 1

        # Print the final state of nums1 after merging
        print("Nums1 After: ", nums1)


# Time Complexity: O(m + n) because we are traversing through both arrays only once.

# Example usage of the solution:
sol = Solution()
sol.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)

# Expected Output: Nums1 After: [1, 2, 2, 3, 5, 6]