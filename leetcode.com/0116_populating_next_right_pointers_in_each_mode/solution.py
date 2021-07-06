"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = [root]

        while len(q) > 0:
            nq = []

            # BFS
            while len(q) > 0:
                node = q.pop(0)

                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)

            for n1, n2 in zip(nq, nq[1:]):
                n1.next = n2

            q = nq

        return root
