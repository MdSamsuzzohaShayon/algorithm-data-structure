"""
Tutorial-1: https://www.youtube.com/watch?v=5iSZ7mh_RAk
Tutorial-2: https://youtu.be/kFeXwkgnQ9U



1. Introduction to Quick Sort
------------------------------
Quick Sort is a highly efficient sorting algorithm and is based on partitioning of an array of data into smaller arrays.
A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot,
based on which the partition is made and another array holds values greater than the pivot value. 
Quick Sort partitions an array and then calls itself recursively twice to sort the two resulting subarrays. 
This algorithm is quite efficient for large-sized data sets as its average and worst-case complexity are O(n^2), respectively.

2. How Quick Sort Works
-----------------------
Quick Sort works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays,
according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.
This can be done in-place, requiring small additional amounts of memory to perform the sorting.

3. Choosing a Pivot
-------------------
There are many different versions of quick sort that pick pivot in different ways:
1. Always pick the first element as a pivot.
2. Always pick the last element as a pivot.
3. Pick a random element as a pivot.
4. Pick the median as the pivot.
The key process in quick sort is the partition process. 

4. Partitioning Process
-----------------------
The logic is to place the pivot element in its correct position in a sorted array and to place all smaller elements 
(smaller than pivot) to the left of the pivot and all greater elements to the right of the pivot.
Here's the step-by-step partitioning process:
1. Choose the rightmost element as the pivot (common practice).
2. Initialize two pointers: left (points to the start) and right (points to the second last element).
3. Move the left pointer to the right until an element greater than or equal to the pivot is found.
4. Move the right pointer to the left until an element less than or equal to the pivot is found.
5. If the left pointer is less than or equal to the right pointer, swap the elements and repeat steps 3 and 4.
6. Finally, swap the pivot element with the element pointed to by the left pointer.

5. Recursive Quick Sort
------------------------
After partitioning, the pivot is now in its final sorted position. Recursively apply the above steps to the sub-arrays
of elements with smaller and greater values.

6. Time Complexity
-------------------
The time complexity of Quick Sort is as follows:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n^2)
However, with good pivot selection, the worst-case complexity is rare.

7. Space Complexity
--------------------
Quick Sort has a space complexity of O(log n) due to the stack space used by recursion.

"""
from typing import List


# https://youtu.be/kFeXwkgnQ9U
def quick_sort(sequence: List[int]) -> List[int]:
    # Get the length of the input sequence (list)
    length: int = len(sequence)

    # Base case: if the sequence has 0 or 1 element, it's already sorted, so return it
    if length <= 1:
        return sequence
    else:
        # Choose the last element as the pivot and remove it from the sequence
        pivot: int = sequence.pop()

    # Initialize two lists to hold elements greater and less than the pivot
    items_greater: List[int] = []
    items_lower: List[int] = []

    # Iterate over each element in the sequence (excluding the pivot)
    for item in sequence:
        # If the item is greater than the pivot, add it to the items_greater list
        if item > pivot:
            items_greater.append(item)
        # If the item is less than or equal to the pivot, add it to the items_lower list
        else:
            items_lower.append(item)

    # Recursively apply quick_sort to the items_lower and items_greater lists
    # Combine the sorted items_lower, pivot, and sorted items_greater to form the final sorted list
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


# Example usage:
print(quick_sort([1, 7, 5, 9, 8, 2, 0, 6, 3, 4]))


# https://youtu.be/5iSZ7mh_RAk
# Implementation of Quick Sort in Python using Hoare's partition scheme

# Function to swap two elements in an array
def swap(a, b, arr):
    # Only swap if the indices are different
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


# Recursive Quick Sort function
def quick_sort_two(elements, start, end):
    # Base case: if the starting index is less than the ending index
    if start < end:
        # Partition the array and get the pivot index
        pi = partition(elements, start, end)
        # Recursively apply Quick Sort to the left subarray
        quick_sort_two(elements, start, pi - 1)
        # Recursively apply Quick Sort to the right subarray
        quick_sort_two(elements, pi + 1, end)


# Partition function using Hoare's partition scheme
def partition(elements, start, end):
    # Choose the first element as the pivot
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        # Move the start index to the right until an element greater than the pivot is found
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        # Move the end index to the left until an element less than or equal to the pivot is found
        while elements[end] > pivot:
            end -= 1
        # If start is less than end, swap the elements at start and end
        if start < end:
            swap(start, end, elements)

    # Swap the pivot element with the element at the end index
    swap(pivot_index, end, elements)

    # Return the end index as the pivot index
    return end


# Example usage
elements = [11, 9, 29, 7, 2, 15, 28]
# Uncomment the following line to test with strings
# elements = ["mona", "dhaval", "aamir", "tina", "chang"]
quick_sort_two(elements, 0, len(elements) - 1)
print(elements)

# Test cases to validate the Quick Sort implementation
tests = [
    [11, 9, 29, 7, 2, 15, 28],
    [3, 7, 9, 11],
    [25, 22, 21, 10],
    [29, 15, 28],
    [],
    [6]
]

# Apply Quick Sort to each test case and print the sorted array
for elements in tests:
    quick_sort_two(elements, 0, len(elements) - 1)
    print(f'Sorted array: {elements}')




"""
Tutorial-3: https://youtu.be/4xbWSRZHqac
Leetcode: https://leetcode.com/problems/sort-colors/description/

75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.


Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]
 

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i<= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1

            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1

            i += 1

        # can not return
        print(nums)


sol = Solution()
print("===== Quicksort Partition =====")
sol.sortColors([2,0,2,1,1,0])




