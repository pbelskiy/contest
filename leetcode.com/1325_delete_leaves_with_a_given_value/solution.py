class Solution:
    # 13 minutes for solution

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        def dfs(node):
            if not node:
                return

            if node.left is node.right is None:
                return node.val == target

            if dfs(node.left):
                node.left = None

            if dfs(node.right):
                node.right = None

            return node.left is node.right is None and node.val == target

        if dfs(root):
            return None

        return root
