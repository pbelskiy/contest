class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        self._dfs(root)
        self.index = 0

    def _dfs(self, node):
        if not node:
            return
        self._dfs(node.left)
        self.values.append(node.val)
        self._dfs(node.right)

    def next(self) -> int:
        self.index += 1
        return self.values[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.values)
