"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example-1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example-2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/
YouTube Tutorial: https://www.youtube.com/watch?v=A2_ldqM4QcY&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=8
"""

from typing import Optional

# Definition of the ListNode class representing a node in a linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Definition of the Solution class with the middleNode function
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow and fast pointers to the head of the linked list
        slow, fast = head, head
        # Move the fast pointer two steps and the slow pointer one step until the fast pointer reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Return the slow pointer, which now points to the middle node
        return slow

# Example 1: Input: head = [1,2,3,4,5,6], Output: [4,5,6]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

# Create an instance of the Solution class
solution1 = Solution()
# Find the middle node for Example 1
result1 = solution1.middleNode(head1)

# Print the result for Example 1
if result1:
    print("Example 1 - The middle node values are:")
    while result1:
        print(result1.value, end=" ")
        result1 = result1.next
else:
    print("Example 1 - The linked list is empty.")

# Example 2: Input: head = [1,2,3,4,5], Output: [3,4,5]
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Create an instance of the Solution class
solution2 = Solution()
# Find the middle node for Example 2
result2 = solution2.middleNode(head2)

# Print the result for Example 2
if result2:
    print("\nExample 2 - The middle node values are:")
    while result2:
        print(result2.value, end=" ")
        result2 = result2.next
else:
    print("Example 2 - The linked list is empty.")
