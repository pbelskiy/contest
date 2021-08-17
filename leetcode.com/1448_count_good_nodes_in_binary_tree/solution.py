class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, val):
            nonlocal count

            if node.val >= val:
                count += 1

            if node.left:
                dfs(node.left, max(val, node.val))

            if node.right:
                dfs(node.right, max(val, node.val))

        dfs(root, root.val)
        return count
