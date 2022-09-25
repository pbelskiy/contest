class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        def build(i, j):
            if i > j:
                return

            mid = (i + j) // 2
            node = TreeNode(values[mid])
            node.left = build(i, mid - 1)
            node.right = build(mid + 1, j)
            return node

        values = []
        dfs(root)
        values.sort()
        return build(0, len(values) - 1)
