class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if node:
                values.append(node.val)
                dfs(node.left)
                dfs(node.right)

        values = []
        dfs(root)
        values.sort()

        root = prev = TreeNode()
        for v in values:
            prev.right = TreeNode(v)
            prev = prev.right

        return root.right
