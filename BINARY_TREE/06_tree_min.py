# 01:20:00 - YouTube Tutorial https://www.youtube.com/watch?v=fAAZixBzIAI

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

