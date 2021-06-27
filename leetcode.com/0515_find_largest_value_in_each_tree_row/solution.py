# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    X = -2**32

    def trace(self, node, idx):
        if not node:
            return

        self.rows[idx] = max(self.rows[idx], node.val)
        self.trace(node.left, idx + 1)
        self.trace(node.right, idx + 1)

    def largestValues(self, root: TreeNode) -> List[int]:
        self.rows = [self.X for _ in range(10**4)]
        self.trace(root, 0)
        return filter(lambda v: v is not self.X, self.rows)
