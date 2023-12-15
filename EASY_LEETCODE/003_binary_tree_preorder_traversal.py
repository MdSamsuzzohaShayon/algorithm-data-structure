"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,2,3]

Example 2:
    Input: root = []
    Output: []

YouTube Tutorial: https://www.youtube.com/watch?v=afTpieEZXck&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=3
LeetCode: https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(3)
b = TreeNode(4)
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr, stack = root, []
        res = []
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        return res


sol = Solution()
print(sol.preorderTraversal(a))
# Big-O = O(n)
