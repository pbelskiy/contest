class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = []
        q = collections.deque([root])

        while q:
            level = []

            nq = collections.deque()
            while q:
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)

            if len(level) > 0:
                levels.append(level)
            q = nq


        ml = None
        mv = -10**6
        for i, l in enumerate(levels):
            if sum(l) > mv:
                mv = sum(l)
                ml = i + 1

        return ml
