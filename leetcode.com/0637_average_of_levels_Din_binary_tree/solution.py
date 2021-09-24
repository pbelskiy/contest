class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque([root])
        levels = []

        while q:
            count = 0
            total = 0
            nq = collections.deque()

            while q:
                node = q.popleft()

                if not node:
                    continue

                nq.append(node.left)
                nq.append(node.right)

                count += 1
                total += node.val

            q = nq
            if count > 0:
                levels.append(total / count)

        return levels
