# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if root.left == root.right == None:
            return (targetSum - root.val == 0)

        if self.hasPathSum(root.left, targetSum - root.val):
            return True

        if self.hasPathSum(root.right, targetSum - root.val):
            return True

        return False

