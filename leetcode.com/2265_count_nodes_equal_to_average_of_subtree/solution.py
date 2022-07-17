class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, 0

            v1, c1 = dfs(node.left)
            v2, c2 = dfs(node.right)

            v = node.val + v1 + v2
            c = 1 + c1 + c2

            if node.val == v // c:
                self.total += 1

            return v, c

        self.total = 0
        dfs(root)
        return self.total
