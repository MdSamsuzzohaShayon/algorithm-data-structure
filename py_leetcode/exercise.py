from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


def test_remove_element():
    solution = Solution()

    # Test Case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"Test Case 1: k = {k1}, nums = {nums1[:k1]}")  # Output should be k = 2, nums = [2, 2]

    # Test Case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Test Case 2: k = {k2}, nums = {nums2[:k2]}")  # Output should be k = 5, nums = [0, 1, 3, 0, 4]


test_remove_element()
