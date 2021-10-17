class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return

            if node.val == target.val:
                return node

            if t := dfs(node.left):
                return t

            if t := dfs(node.right):
                return t

        return dfs(cloned)
