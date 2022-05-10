class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        def add(node):
            if node and node.val not in to_delete:
                forest.append(node)

        def dfs(node):
            if node.val in to_delete:
                add(node.left)
                add(node.right)

            if node.left:
                dfs(node.left)
                if node.left.val in to_delete:
                    node.left = None

            if node.right:
                dfs(node.right)
                if node.right.val in to_delete:
                    node.right = None

        forest = []
        to_delete = set(to_delete)
        add(root)
        dfs(root)
        return forest
