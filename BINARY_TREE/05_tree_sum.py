# 01:05:00 - YouTube Tutorial https://www.youtube.com/watch?v=fAAZixBzIAI

#                    a
#                  /  \
#                b     c
#              / \      \
#            d    e      f

from typing import List

class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left: Node | None = None
        self.right: Node | None = None


a = Node(2)
b = Node(5)
c = Node(6)
d = Node(4)
e = Node(8)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def treeSumRecursive(root: Node) -> int:
    if root is None:
        return 0
    return root.val + treeSumRecursive(root.left) + treeSumRecursive(root.right)


print(treeSumRecursive(a))


def treeSumIterative(root: Node) -> int:
    if root is None:
        return 0
    totalSum: int = 0
    queue: List[Node] = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        totalSum += current.val
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return totalSum


print(treeSumIterative(a))
