# 00:06:49 - YouTube https://www.youtube.com/watch?v=fAAZixBzIAI
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Create Nodes
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

# Connecting nodes
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

"""
            a 
           /  \
         b     c
        / \     \
       d   e     f
"""