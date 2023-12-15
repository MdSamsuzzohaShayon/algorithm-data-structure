"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [3,2,1]

Example 2:
    Input: root = []
    Output: []

YouTube Tutorial: https://www.youtube.com/watch?v=QhszUQhGGlA&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=2
LeetCode: https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val: int = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit: List[bool] = [False]
        res = []

        while stack:
            curr = stack[-1]
            v = visit[-1]
            if curr:
                if v:
                    res.append(curr.val)
                    stack.pop()
                    visit.pop()
                else:
                    visit[-1] = True
                    if curr.right:
                        stack.append(curr.right)
                        visit.append(False)
                    if curr.left:
                        stack.append(curr.left)
                        visit.append(False)
            else:
                stack.pop()
                visit.pop()

        return res


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.right = b
b.left = c

sol = Solution()
print(sol.postorderTraversal(a))

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

sol = Solution()
print(sol.postorderTraversal(a))
