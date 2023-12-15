"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true

Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

YouTube Tutorial: https://www.youtube.com/watch?v=Mao9uzxwvmc&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=5
LeetCode Problem: https://leetcode.com/problems/symmetric-tree/
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(5)
d = TreeNode(6)
e = TreeNode(7)
f = TreeNode(9)

a.left = b
a.right = c
b.left = d
c.right = f
c.left = e


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            # Compare values of left node and values of right node
            # Compare left subtree with right subtree
            # Compare inner subtree
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)

sol = Solution()
print(sol.isSymmetric(a))
# Big-O = O(n)
