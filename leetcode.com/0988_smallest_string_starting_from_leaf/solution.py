class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def dfs(node, path):
            if node.left is node.right is None:
                s.append((path + chr(ord('a') + node.val))[::-1])
                return

            if node.left:
                dfs(node.left, path + chr(ord('a') + node.val))

            if node.right:
                dfs(node.right, path + chr(ord('a') + node.val))

        s = []
        dfs(root, '')
        return min(s)
