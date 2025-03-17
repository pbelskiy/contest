"""
Use simple segment tree to find leftmost max backet.

TC: O(NlgN)
SC: O(N)
"""
class Node:

    def __init__(self, left, right, value) -> None:
        self.left = left
        self.right = right
        self.value = value


class Solution:

    def _build(self, a):
        if not a:
            return

        if len(a) == 1:
            left, right = [], []
        else:
            left, right = a[:len(a) // 2], a[len(a) // 2:]

        return Node(self._build(left), self._build(right), max(a))

    def _update(self, node, t):
        if not node:
            return False

        if node.left is None and node.right is None and node.value >= t:
            node.value = 0  # make basket empty
            return True

        r = False

        if node.left and node.left.value >= t:
            r |= self._update(node.left, t)
        else:
            r |= self._update(node.right, t)

        if r:
            node.value = max(node.left.value if node.left else 0,
                             node.right.value if node.right else 0)

        return r

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        t = 0
        self.root = self._build(baskets)

        for f in fruits:
            if not self._update(self.root, f):
                t += 1

        return t

