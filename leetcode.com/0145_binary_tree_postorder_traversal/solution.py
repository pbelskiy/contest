class Solution:
    def dfs(self, node):
        if not node:
            return

        self.dfs(node.left)
        self.dfs(node.right)
        self.values.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.values = []
        self.dfs(root)
        return self.values
