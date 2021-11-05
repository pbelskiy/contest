class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node, r, c):
            if not node:
                return
            columns[c][r].append(node.val)
            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)

        columns = collections.defaultdict(lambda: collections.defaultdict(list))
        dfs(root, 0, 0)

        ordered = []

        for row in sorted(columns.keys()):
            column = []
            for k in sorted(columns[row].keys()):
                column.extend(sorted(columns[row][k]))
            ordered.append(column)

        return ordered
