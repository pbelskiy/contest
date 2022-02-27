
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            s.append(str(node.val))

            if node.left:
                s.append('(')
                dfs(node.left)
                s.append(')')
            elif node.right:
                s.append('()')

            if node.right:
                s.append('(')
                dfs(node.right)
                s.append(')')

        s = []
        dfs(root)
        return ''.join(s)
