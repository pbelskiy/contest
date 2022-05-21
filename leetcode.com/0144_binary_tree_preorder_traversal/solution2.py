class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        v = []
        q = deque([root])
        while q:
            node = q.pop()
            if not node:
                continue

            v.append(node.val)
            q.append(node.right)
            q.append(node.left)

        return v
