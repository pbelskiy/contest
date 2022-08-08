class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = deque([0])
        visited = set([0])

        while queue:
            v = queue.popleft()

            for n in graph[v]:
                if n in restricted:
                    continue
                if n in visited:
                    continue

                queue.append(n)
                visited.add(n)

        return len(visited)
