class Solution:
    def isValidBST(self, root: Optional[TreeNode], left = -2**32, right = 2**32) -> bool:

        if not root:
            return True

        if not (left < root.val < right):
            return False

        return self.isValidBST(root.left, left, root.val) and \
               self.isValidBST(root.right, root.val, right)
