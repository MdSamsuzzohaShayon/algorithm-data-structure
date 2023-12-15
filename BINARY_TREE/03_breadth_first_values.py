# 00:36:00 - YouTube Tutorial https://www.youtube.com/watch?v=fAAZixBzIAI

#                    a
#                  /  \
#                b     c
#              / \      \
#            d    e      f

"""
Result be like: a, b, c, d, e, f
Use queue data structure for this
n = # of nodes
Time: 0(n) because each node is processed once.
Space: 0(n) because, in the worst case, all nodes could be in the queue at once.
"""
from typing import List


class Node:
    def __init__(self, val: str):
        self.val = val
        self.left = None
        self.right = None


# Making tree
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


def breadthFirstValues(root: Node):
    if root is None:
        return []

    values: List[str] = []
    queue_list: List[Node] = [root]

    while len(queue_list) > 0:
        # Remove front of the queue that is index 0
        current = queue_list.pop(0)
        values.append(current.val)
        if current.left is not None:
            queue_list.append(current.left)
        if current.right is not None:
            queue_list.append(current.right)

    return values


print(breadthFirstValues(a))
