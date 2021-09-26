class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, path):
            if node.left is node.right is None:
                return int(''.join(map(str, path + [node.val])))

            total = 0

            if node.left:
                total += dfs(node.left, path[:] + [node.val])

            if node.right:
                total += dfs(node.right, path[:] + [node.val])

            return total

        return dfs(root, [])
