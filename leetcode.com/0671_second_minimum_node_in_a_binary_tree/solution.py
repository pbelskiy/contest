class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        def bfs(node):
            if not node:
                return

            values.add(node.val)
            bfs(node.left)
            bfs(node.right)

        values = set()
        bfs(root)

        if len(values) < 2:
            return -1

        return sorted(values)[1]
