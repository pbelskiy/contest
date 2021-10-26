class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 1

            return dfs(node.left) + dfs(node.right)

        return dfs(root) - 1
