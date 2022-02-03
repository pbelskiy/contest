class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def bfs(node):
            if not node:
                return

            values.append(node.val)
            bfs(node.left)
            bfs(node.right)

        values = []
        bfs(root)
        values.sort()
        return values[k - 1]
