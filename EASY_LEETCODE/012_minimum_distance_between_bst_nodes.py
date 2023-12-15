"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:
    Input: root = [4,2,6,1,3]
    Output: 1

Example 2:
    Input: root = [1,0,48,null,null,12,49]
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [2, 100].
    0 <= Node.val <= 105

LeetCode: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
YouTube Tutorial: https://www.youtube.com/watch?v=joxx4hTYwcw&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=10
"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev: None | TreeNode = None
        result: int | float = float('inf')

        def dfs(node):
            if not node:
                return
            nonlocal prev, result
            dfs(node.left)
            if prev:
                result = min(result, node.val - prev.val)
            prev = node
            dfs(node.right)

        dfs(root)
        return result


# Instantiate the Solution class.
solution = Solution()

# Example 1
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

result1 = solution.minDiffInBST(root1)
print("Example 1:", result1)

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(48)
root2.right.left = TreeNode(12)
root2.right.right = TreeNode(49)

result2 = solution.minDiffInBST(root2)
print("Example 2:", result2)