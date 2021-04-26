# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        s = 0

        if root.left:
            if root.left.left == None and root.left.right == None:
                s += root.left.val
            else:
                s += self.sumOfLeftLeaves(root.left)

        if root.right:
            s += self.sumOfLeftLeaves(root.right)

        return s
