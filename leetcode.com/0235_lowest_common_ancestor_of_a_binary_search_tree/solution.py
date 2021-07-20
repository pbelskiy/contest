# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def get_trace(target):
            trace = {}
            node = root
            while node:
                trace[node.val] = node
                if node == target:
                    break

                if node.val < target.val:
                    node = node.right
                else:
                    node = node.left

            return trace

        pt = get_trace(p)
        qt = get_trace(q)

        sqt = set(qt.keys())
        for v in reversed(pt):
            if v in sqt:
                return pt[v]
