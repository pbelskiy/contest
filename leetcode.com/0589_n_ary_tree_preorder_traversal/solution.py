class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        def dfs(node):
            if not node:
                return
            values.append(node.val)
            for child in node.children:
                dfs(child)

        values = []
        dfs(root)
        return values
