"""
Find target (X) node and count of nodes in all three directions
left, right and parent. Then calculate our win rate.

TC: O(N)
SC: O(N)
"""
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        def find(node, val):
            if not node:
                return
            if node.val == val:
                return node
            return find(node.left, val) or find(node.right, val)

        def count(node):
            if not node:
                return 0
            return count(node.left) + count(node.right) + 1

        node = find(root, x)

        left = count(node.left)
        right = count(node.right)
        parent = n - left - right - 1

        # we go upper and win
        if parent > left + right:
            return True

        # we go left and win
        if left > parent + right:
            return True

        # we go right and win
        if right > parent + left:
            return True

        return False
