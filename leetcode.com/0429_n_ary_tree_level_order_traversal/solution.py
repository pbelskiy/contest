class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []
        q = collections.deque([root])

        while q:
            level = []

            nq = collections.deque()
            while q:
                node = q.popleft()
                if node is None:
                    break
                level.append(node.val)

                for child in node.children:
                    nq.append(child)

            if len(level) > 0:
                levels.append(level)
            q = nq

        return levels
