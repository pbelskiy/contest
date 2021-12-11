class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        while root:
            if root.val == val:
                return root

            if root.val > val:
                root = root.left
            else:
                root = root.right

        return None
