from typing import List

"""
Tutorial-1: https://youtu.be/mB5HXBb_HY8
Tutorial-2: https://youtu.be/cVZMah9kEjI
Tutorial-3: https://youtu.be/MsYZSinhuFo

Merge Sort Algorithm

Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, 
recursively sorts each half, and then merges the two sorted halves into a single sorted array.

The algorithm can be broken down into the following steps:

1. Divide: Split the array into two halves.
2. Conquer: Recursively sort each half.
3. Combine: Merge the two sorted halves into a single sorted array.

Detailed Explanation:

Step 1: Divide
The array is divided into two halves using the middle index. 
If the array has an odd number of elements, the middle index will split it into two nearly equal halves.

Step 2: Conquer
Each half is recursively sorted using the Merge Sort algorithm. 
This continues until the base case is reached, where the array has only one element or is empty, 
and is therefore considered sorted.

Step 3: Combine
The two sorted halves are merged into a single sorted array. 
This is done by comparing the smallest elements of each half and adding the smaller element to the merged array, 
and repeating this process until all elements from both halves are added to the merged array.

Base Case:
The base case of the recursion is when the array has one element or is empty. 
In this case, the array is already sorted and is returned as is.

Time Complexity:
The time complexity of Merge Sort is O(n log n), where n is the number of elements in the array.
This is because the array is divided into two halves (log n) times, and merging the halves takes linear time (n).

Space Complexity:
The space complexity of Merge Sort is O(n) because it requires additional space to store the temporary arrays during merging.
"""


# Define the merge_sort function which takes a list of integers as input.
def recursive_merge_sort(arr: List[int]):
    # If the array has more than one element, proceed to split and sort it.
    if len(arr) > 1:
        # Divide the array into two halves.
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        # Recursively call merge_sort on each half to sort them.
        recursive_merge_sort(left_arr)
        recursive_merge_sort(right_arr)

        # Initialize three indices to keep track of the current position
        # in the left array (i), right array (j), and the merged array (k).
        i = 0  # left array index
        j = 0  # right array index
        k = 0  # merged array index

        # Merge the two sorted halves into a single sorted array.
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                # If the current element in the left array is smaller,
                # add it to the merged array.
                arr[k] = left_arr[i]
                i += 1  # Move the index of the left array forward.
            else:
                # If the current element in the right array is smaller or equal,
                # add it to the merged array.
                arr[k] = right_arr[j]
                j += 1  # Move the index of the right array forward.
            k += 1  # Move the index of the merged array forward.

        # If there are any remaining elements in the left array, add them to the merged array.
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # If there are any remaining elements in the right array,
        # add them to the merged array.
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


# Test the merge_sort function with a sample array.
arr_test: List[int] = [3, 4, 6, 5, 6, 2, 3, 8, 0, 1, 0, 3, 8, 2, 7, 9, 1]
recursive_merge_sort(arr_test)
print(arr_test)  # Output: [0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9]


"""
Tutorial-1: https://youtu.be/xleF7ykgcHY
Tutorial-2: https://youtu.be/3j0SWDX4AtU

ite_list = [8, 3, 7, 4, 9, 2, 6, 5] # length 8
This list need to be4 divided into 8 different lists, each list contains 1 element. If there is only one element in a list it is sorted by default.
If the array is sorted we can merge them into another array. We need to pick up 2 list at a time and merge them

Iterative Merge Sort
Explanation:
- Merge Sort is a divide-and-conquer algorithm that works by dividing the array into smaller subarrays, sorting those subarrays, and then merging them back together.
- Unlike the recursive version, the iterative version of merge sort sorts the array in a bottom-up manner, starting with smaller subarrays and gradually merging them into larger sorted subarrays.

"""


def iterative_merge_sort(arr: List[int]) -> List[int]:
    # Get the length of the array
    n = len(arr)

    # Start with subarrays of size 1, then 2, 4, 8, etc.
    curr_size = 1

    # Outer loop for the size of subarrays to be merged
    while curr_size < n:

        # Inner loop for selecting subarray pairs to be merged
        # Left subarray starts from index left
        left = 0
        while left < n:
            # Calculate the middle point and the end of the right subarray
            mid = min(left + curr_size - 1, n - 1)
            right = min(left + 2 * curr_size - 1, n - 1)

            # Merge the two subarrays [left...mid] and [mid+1...right]
            merge(arr, left, mid, right)

            # Move to the next pair of subarrays
            left += 2 * curr_size

        # Increase the size of the subarrays to be merged
        curr_size *= 2

    return arr


def merge(arr: List[int], left: int, mid: int, right: int) -> None:
    """
    This function merges two sorted subarrays of arr.
    The first subarray is arr[left:mid+1].
    The second subarray is arr[mid+1:right+1].
    """

    # Create temporary arrays to hold the elements of the subarrays
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]

    # Initialize pointers for left_subarray, right_subarray, and the main array
    i, j, k = 0, 0, left

    # Merge the subarrays back into the original array in sorted order
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1
        k += 1

    # Copy any remaining elements of left_subarray (if any)
    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1

    # Copy any remaining elements of right_subarray (if any)
    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1


# Example usage of the iterative merge sort:
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)

sorted_arr = iterative_merge_sort(arr)
print("Sorted array:", sorted_arr)

# Expected Output:
# Original array: [12, 11, 13, 5, 6, 7]
# Sorted array: [5, 6, 7, 11, 12, 13]


"""
Youtube: https://youtu.be/MsYZSinhuFo
Leetcode: https://leetcode.com/problems/sort-an-array/description/

912. Sort an Array
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]
    Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]
    Explanation: Note that the values of nums are not necessary unique.
 
Constraints:
    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1

            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def merge_sort_two(arr, l, r):
            if l == r:
                return arr

            m = (l+r) // 2
            merge_sort_two(arr, l, m)
            merge_sort_two(arr, m+1, r)

            merge(arr, l, m, r)
            return arr

        return merge_sort_two(nums, 0, len(nums)-1)


sol = Solution()
arr_test_two: List[int] = [3, 4, 6, 5, 6, 2, 3, 8, 0, 1, 0, 3, 8, 2, 7, 9, 1]
print(sol.sortArray(arr_test_two))