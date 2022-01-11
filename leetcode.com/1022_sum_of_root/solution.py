class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def dfs(node, v):
            if not node:
                return

            if node.left is node.right is None:
                self.total += int(v + str(node.val), 2)
                return

            dfs(node.left, v + str(node.val))
            dfs(node.right, v + str(node.val))

        self.total = 0
        dfs(root, '')
        return self.total
