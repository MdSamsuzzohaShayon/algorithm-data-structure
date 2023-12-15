# 00:14:20 - YouTube Tutorial https://www.youtube.com/watch?v=fAAZixBzIAI

#                    a
#                  /  \
#                b     c
#              / \      \
#            d    e      f

from typing import List


class Node:
    def __init__(self, val: str):
        self.val = val
        self.left = None
        self.right = None


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


# Iterative solution
def depthFirstValuesIterative(root: Node) -> List[str]:
    if root is None:
        return []
    result: List[str] = []
    stack: List[Node] = [root]  # Last element of the stack is the top

    while len(stack) > 0:
        current: Node = stack.pop()  # get top and remove from the stack
        print(current.val)
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result


res1 = depthFirstValuesIterative(a)
print(res1)


# Recursive solution
def depthFirstValuesRecursive(root: Node) -> List[str]:
    if root is None:
        return []
    leftValues = depthFirstValuesRecursive(root.left)  # [b, d, e]
    rightValues = depthFirstValuesRecursive(root.right)  # [c, f]
    return [root.val] + leftValues + rightValues


res2 = depthFirstValuesRecursive(a)
print(res2)
