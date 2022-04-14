class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()

        def dfs(node):
            if not node:
                return

            self.values.add(node.val)

            if node.left:
                node.left.val = 2*node.val + 1

            if node.right:
                node.right.val = 2*node.val + 2

            dfs(node.left)
            dfs(node.right)

        root.val = 0
        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.values
