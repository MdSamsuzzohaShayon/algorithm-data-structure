"""
Tutorial: https://www.youtube.com/watch?v=nKzEJWbkPbQ
Insertion sort is a simple and intuitive comparison-based sorting algorithm that builds the final sorted array one item at a time. It is much like the way you might sort
playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position
in the sorted part.

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
Insertion sort is more efficient than bubble sort for small datasets or lists that are already partially sorted. Its simplicity and efficiency for nearly sorted data
make it useful in practice for specific scenarios, such as sorting small arrays or when adding elements to a sorted list.

Iteration best O(n) and iteration worst O(n)
Shift items best O(1) and iteration worst O(n)
Best case scenario O(n
Worst case scenario O(n^2
"""

from typing import List


# Define the insertion_sort function which takes a list of integers
def insertion_sort(elements: List[int]):
    # Get the number of elements in the list
    size = len(elements)

    # Loop through each element in the list starting from the first
    for i in range(size):
        # The current element to be inserted into the sorted portion
        curr = elements[i]
        # The position just before the current element
        j = i - 1

        # Move elements of the sorted portion that are greater than
        # the current element one position to the right
        while j >= 0 and elements[j] > curr:
            # Shift the element to the right
            elements[j + 1] = elements[j]
            # Move one position to the left
            j -= 1

        # Insert the current element into its correct position
        elements[j + 1] = curr


# Main block to execute when the script is run directly
# if __name__ == "__main__":

# Example list of elements to be sorted
elements = [5, 8, 3, 6, 8, 12, 3]
# Call the insertion_sort function to sort the list
insertion_sort(elements)
# Print the sorted list
print(elements)

"""
Tutorial: https://www.youtube.com/watch?v=Kk6mXAzqX3Y
Leetcode: https://leetcode.com/problems/insertion-sort-list/description/

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:
    1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
    3. It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the 
input data and inserted in-place into the sorted list with each iteration.

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]
    
    
Big-O notation 
Worse case time complexity O(n^2)
Best case time complexity O(n)
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that acts as a new head for the sorted part of the list
        dummy = ListNode(0, head)

        # Initialize prev to point to the head of the original list and curr to the second node
        prev, curr = head, head.next

        # Iterate over the list until curr becomes None (end of the list)
        while curr:
            # If the current value is greater than or equal to the previous value,
            # it is already in the correct position in the sorted list
            if curr.val >= prev.val:
                # Move prev and curr pointers one step forward
                prev, curr = curr, curr.next
                continue

            # Otherwise, find the correct position for the current node in the sorted part
            # Start from the dummy node
            temp = dummy

            # Find the insertion point in the sorted list for curr node
            while curr.val > temp.next.val:
                temp = temp.next

            # Insert curr in the sorted part of the list
            # Disconnect curr from the unsorted part
            prev.next = curr.next
            # Connect curr to the sorted part
            curr.next = temp.next
            temp.next = curr
            # Move curr to the next node in the unsorted part
            curr = prev.next

        # Return the new head of the sorted list, which is dummy's next node
        return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


print("===== Insertion Sort =====")
# Example input
input_values = [4, 2, 1, 3]
head = create_linked_list(input_values)

# Solution instance
solution = Solution()

# Sort the list
sorted_head = solution.insertionSortList(head)

# Print the sorted linked list
print_linked_list(sorted_head)
