class Solution:
    def dfs(self, node):
        if not node:
            return

        self.values.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.values = []
        self.dfs(root)
        return self.values
