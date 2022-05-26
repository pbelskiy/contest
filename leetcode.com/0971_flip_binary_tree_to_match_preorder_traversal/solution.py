class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        i = 0
        flipped = []
        q = collections.deque([(root)])
        while q:
            node = q.pop()
            if not node:
                continue

            if node.val != voyage[i]:
                return [-1]

            if node.right and node.right.val == voyage[i + 1] and node.left is not None:
                flipped.append(node.val)
                q.extend([node.left, node.right])
            else:
                q.extend([node.right, node.left])

            i += 1

        return flipped
