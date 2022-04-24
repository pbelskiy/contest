class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            values.append(node.val)

        values = []
        dfs(root)
        return values
