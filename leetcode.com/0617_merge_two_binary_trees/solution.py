class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(n1, n2):
            if not (n1 and n2):
                return

            if n1 and n2:
                n1.val += n2.val

            if n1.right is None and n2.right:
                n1.right = n2.right
            else:
                dfs(n1.right, n2.right)

            if n1.left is None and n2.left:
                n1.left = n2.left
            else:
                dfs(n1.left, n2.left)

        if not root1:
            root1, root2 = root2, root1

        dfs(root1, root2)
        return root1
