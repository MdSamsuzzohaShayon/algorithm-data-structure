"""
Tutorial: https://www.youtube.com/watch?v=Ber2pi2C0j0
Leetcode: https://leetcode.com/problems/search-a-2d-matrix/description/
Neetcode: https://neetcode.io/problems/search-2d-matrix

Search 2D Matrix
    You are given an m x n 2-D integer array matrix and an integer target.
    Each row in matrix is sorted in non-decreasing order.
    The first integer of every row is greater than the last integer of the previous row.
    Return true if target exists within matrix or false otherwise.
    Can you write a solution that runs in O(log(m * n)) time?

Example 1:
    Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
    Output: true
    
Example 2:
    Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
    Output: false
    
Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10000 <= matrix[i][j], target <= 10000
"""

from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # Top rows and bottom rows
        top, bottom = 0, rows - 1
        while top <= bottom:
            middle_row = (top + bottom) // 2
            if target > matrix[middle_row][-1]:
                top = middle_row + 1
            elif target < matrix[middle_row][0]:
                bottom = middle_row - 1
            else:
                break

        if not (top <= bottom):
            return False

        middle_row = (top + bottom) // 2
        left, right = 0, cols - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[middle_row][middle]:
                left = middle + 1
            elif target < matrix[middle_row][middle]:
                right = middle - 1
            else:
                return True

        return False


matrix_1 = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target_1 = 15
sol = Solution()
case_1 = sol.searchMatrix(matrix=matrix_1, target=target_1)
print({"Case-1": case_1})

matrix_2 = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target_2 = 10
case_2 = sol.searchMatrix(matrix=matrix_2, target=target_2)
print({"Case-2": case_2})

"""
Youtube: https://www.youtube.com/watch?v=0A40XJH_VvE
Leetcode: https://leetcode.com/problems/search-insert-position/description/
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3: 
    Input: nums = [1,3,5,6], target = 7
    Output: 4
"""


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = None
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


sol2 = Solution2()
nums = [1, 3, 5, 6]
sol2_case_1 = sol2.searchInsert(nums, 5)
print({'sol2_case_1': sol2_case_1})  # Exp: 2
sol2_case_2 = sol2.searchInsert(nums, 2)  # Exp 1
print({'sol2_case_2': sol2_case_2})  # Exp: 1

"""
Youtube: https://www.youtube.com/watch?v=s4DPM8ct1pI
Leetcode: https://leetcode.com/problems/binary-search/description/
704. Binary Search
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
 
Constraints:
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""


class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        # Find mid-point = (left index + right index) / 2
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            # mid_index: int = (left_index + right_index) // 2
            # Another way, this way is better in other programming languages because the integer could be pretty big. It will never overflow
            # left_index - right_index = distance between two pointers
            mid_index: int = left_index + ((right_index - left_index) // 2)
            if nums[mid_index] > target:
                right_index = mid_index - 1
            elif nums[mid_index] < target:
                left_index = mid_index + 1
            else:
                return mid_index

        # if left index is greater than right index that means we are out of the loop, the condition is failed in while loop and we did not found the target value
        return -1


arr = [-1, 0, 3, 5, 9, 12]
sol3 = Solution3()
sol3_case_1 = sol3.search(arr, 9)
print(sol3_case_1)  # Expected 4

# https://www.youtube.com/watch?v=K-RYzDZkzCI
# https://www.youtube.com/watch?v=GnZ9ppr_zaI

"""
YouTube: https://www.youtube.com/watch?v=g_S5WuasWUE
LeetCode: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [1]
    Output: [1]
 

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
 
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution4:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursively Big-O= O(n)
        res: List[int] = []

        def inorder(root: TreeNode):
            # Base case
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res


class Solution5:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative Big-O= O(n)
        res = []
        stack = []
        curr = root
        while curr or stack:
            # It will append to the stack until we get the value of the pointer (curr) null
            while curr:
                stack.append(curr)
                curr = curr.left
            # If you find a node has no children (left or right children) we will drop that
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


# Helper function to build tree from list
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    index = 1
    while queue and index < len(nodes):
        node = queue.pop(0)
        if nodes[index] is not None:
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1
        if index < len(nodes) and nodes[index] is not None:
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1
    return root


sol4 = Solution4()
root1 = build_tree([1, None, 2, 3])
root2 = build_tree([])

print({'inorder_traversal (Recursive): ': sol4.inorderTraversal(root1)})  # Expected [1,3,2]
print({'inorder_traversal (Recursive): ': sol4.inorderTraversal(root2)})  # Expected []

sol5 = Solution5()
print({'inorder_traversal (Iterative): ': sol5.inorderTraversal(root1)})  # Expected [1,3,2]
print({'inorder_traversal (Iterative): ': sol5.inorderTraversal(root2)})  # Expected [1,3,2]
