class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node, arr):
            if not node:
                return arr

            if node.left is node.right is None:
                arr.append(node.val)

            dfs(node.left, arr)
            dfs(node.right, arr)
            return arr

        return dfs(root1, []) == dfs(root2, [])
