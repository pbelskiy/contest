class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(node, path):
            if target in path:
                return True

            if not node:
                return False

            np = path + str(node.val)
            if dfs(node.left, np) or dfs(node.right, np):
                return True

        target = ''
        while head:
            target += str(head.val)
            head = head.next

        return dfs(root, '')
