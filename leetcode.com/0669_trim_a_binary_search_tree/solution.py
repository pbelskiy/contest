class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return

            ret = node
            if not (low <= node.val <= high):
                ret = None

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return ret or node.left or node.right

        return dfs(root)
