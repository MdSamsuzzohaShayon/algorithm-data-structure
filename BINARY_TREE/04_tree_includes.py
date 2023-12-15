# 00:47:40 - YouTube Tutorial https://www.youtube.com/watch?v=fAAZixBzIAI

#                    a
#                  /  \
#                b     c
#              / \      \
#            d    e      f

from typing import List


class Node:
    def __init__(self, val: str):
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


# Method-1:  Iterative Breadth-First search algorithm
def treeIncludesIterative(root: Node, target: str):
    if root is None:
        return False
    queue_list: List[Node] = [root]
    while len(queue_list) > 0:
        current = queue_list.pop(0)  # First element
        if current.val == target:
            return True
        if current.left:
            queue_list.append(current.left)
        if current.right:
            queue_list.append(current.right)

    return False


print(treeIncludesIterative(a, 'e'))
print(treeIncludesIterative(a, 'j'))


# Method-1:  Recursive Breadth-First search algorithm
def treeIncludesRecursive(root: Node, target: str):
    if root is None:
        return False
    if root.val == target:
        return True
    return treeIncludesRecursive(root.left, target) or treeIncludesRecursive(root.right, target)


print(treeIncludesRecursive(a, 'e'))
print(treeIncludesRecursive(a, 'j'))
