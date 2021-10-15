class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(n1, n2):
            if n1 is n2:
                return True

            if (n1 is None and n2 is not None) or (n2 is None and n1 is not None):
                return False

            if n1.val != n2.val:
                return False

            if not dfs(n1.left, n2.right):
                return False

            if not dfs(n1.right, n2.left):
                return False

            return True

        return dfs(root.left, root.right)
