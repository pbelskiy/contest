class Solution:
    def dfs(self, node):
        if not node:
            return

        self.dfs(node.left)
        self.values.append(node.val)
        self.dfs(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.values = []
        self.dfs(root)
        return self.values
