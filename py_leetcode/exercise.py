from typing import List
# The goal is to merge the two arrays in O(m + n) time complexity and store the result in-place in nums1.

"""
Approach:
        - We use a two-pointer technique starting from the end of nums1 and nums2 to merge the arrays in reverse.
        - We start from the back of nums1 and nums2 since nums1 has extra space at the end.
        - We compare elements from the end and insert the larger of the two elements at the correct position.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x, y = m - 1, n - 1

        # Looping all list (nums1 and nums2) in decreasing order
        for z in range(m + n - 1, -1, -1):
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1
            elif y < 0:
                break
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1


sol = Solution()
n1 = [1, 2, 3, 0, 0, 0]
sol.merge(nums1=n1, m=3, nums2=[2, 5, 6], n=3)
print(n1)