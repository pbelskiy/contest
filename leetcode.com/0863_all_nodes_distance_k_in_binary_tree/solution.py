class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def dfs(node, prev):
            if not node:
                return

            if prev:
                graph[node.val].append(prev.val)
            if node.left:
                graph[node.val].append(node.left.val)
            if node.right:
                graph[node.val].append(node.right.val)

            dfs(node.left, node)
            dfs(node.right, node)

        def bfs():
            values = []
            visited = set([target.val])
            q = collections.deque([(target.val, 0)])

            while q:
                v, d = q.popleft()

                if d == k:
                    values.append(v)

                for nv in graph[v]:
                    if nv not in visited:
                        q.append((nv, d + 1))
                        visited.add(nv)

            return values

        graph = collections.defaultdict(list)
        dfs(root, None)
        return bfs()
