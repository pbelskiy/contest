class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node:
                self.values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        self.values = set()
        dfs(root)
        return len(self.values) == 1
