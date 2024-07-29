"""
Tutorial: https://www.youtube.com/watch?v=nKzEJWbkPbQ
Insertion sort is a simple and intuitive comparison-based sorting algorithm that builds the final sorted array one item at a time. It is much like the way you might sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

How Insertion Sort Works
    1. Start with the Second Element: The first element is considered sorted. Take the second element and compare it with the elements in the sorted part (on its left).
    2. Find the Correct Position: Compare the current element with the elements in the sorted part and find the correct position where the current element should be inserted.
    3. Shift Elements: Shift all the larger elements in the sorted part one position to the right to make space for the current element.
    4. Insert the Element: Insert the current element at its correct position.
    5. Repeat: Repeat the process for all remaining elements in the unsorted part.

Example
Let's say we have the following list of numbers to sort in ascending order: [5, 3, 8, 4, 2]

First Pass (consider 3):
    Compare 3 with 5: [5, 5, 8, 4, 2]
    Place 3 in the correct position: [3, 5, 8, 4, 2]

Second Pass (consider 8):
    Compare 8 with 5: [3, 5, 8, 4, 2] (no shift needed)

Third Pass (consider 4):
    Compare 4 with 8: [3, 5, 8, 8, 2]
    Compare 4 with 5: [3, 5, 5, 8, 2]
    Place 4 in the correct position: [3, 4, 5, 8, 2]

Fourth Pass (consider 2):
    Compare 2 with 8: [3, 4, 5, 8, 8]
    Compare 2 with 5: [3, 4, 5, 5, 8]
    Compare 2 with 4: [3, 4, 4, 5, 8]
    Compare 2 with 3: [3, 3, 4, 5, 8]
    Place 2 in the correct position: [2, 3, 4, 5, 8]

Now the list is sorted: [2, 3, 4, 5, 8]


Complexity Analysis
    Time Complexity:
        Worst Case: O(n^2) when the list is in reverse order.
        Best Case:O(n) when the list is already sorted.
        Average Case: O(n^2)
    Space Complexity:
        O(1) since it is an in-place sorting algorithm.
Insertion sort is more efficient than bubble sort for small datasets or lists that are already partially sorted. Its simplicity and efficiency for nearly sorted data make it useful in practice for specific scenarios, such as sorting small arrays or when adding elements to a sorted list.

Iteration best O(n) and iteration worst O(n)
Shift items best O(1) and iteration worst O(n)
Best case scenario O(n
Worst case scenario O(n^2
"""
from typing import List

def insertion_sort(elements: List[int]):
    size  = len(elements)
    for i in range(size):
        curr = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > curr:
            # Shift the item to the right
            elements[j+1] = elements[j]
            j-=1
        elements[j+1] = curr



if __name__ == "__main__":
    elements = [5, 8, 3, 6, 8, 12, 3]
    insertion_sort(elements)
    print(elements)