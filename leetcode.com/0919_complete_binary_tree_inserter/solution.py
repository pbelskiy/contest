class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def insert(self, val: int) -> int:
        q = deque([self.root])
        while q:
            node = q.popleft()

            if node.left is None:
                node.left = TreeNode(val)
                return node.val
            elif node.right is None:
                node.right = TreeNode(val)
                return node.val
            else:
                q.extend([node.left, node.right])

    def get_root(self) -> Optional[TreeNode]:
        return self.root
