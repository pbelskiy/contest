class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def dfs(node):
            return 1 + max(dfs(node.left), dfs(node.right)) if node else 0

        h = dfs(root)
        w = 2**h - 1
        matrix = [[""]*w for _ in range(h)]

        def build(node, c, r):
            if not node:
                return

            matrix[r][c] = str(node.val)

            build(node.left, c - 2**(h-1-r-1), r + 1)
            build(node.right, c + 2**(h-1-r-1), r + 1)

        build(root, w // 2, 0)
        return matrix
