class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return

            if any([dfs(node.left), dfs(node.right)]):
                node.val = 1
            elif node is root:
                self.total += 1
                return

            if (node.left and node.left.val == 0) or (node.right and node.right.val == 0):
                node.val = 1
                self.total += 1
                return True

            return False

        self.total = 0
        dfs(root)
        return self.total

