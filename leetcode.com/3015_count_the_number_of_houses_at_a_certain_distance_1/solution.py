class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:

        def bfs(a, t):
            q = deque([(a, 0)])
            v = set()
            while q:
                a, n = q.popleft()
                if a == t:
                    return n

                for b in g[a]:
                    if b not in v:
                        q.append((b, n + 1))
                        v.add((b))

            return float('inf')

        g = defaultdict(set)

        for i in range(1, n):
            g[i].add(i + 1)
            g[i + 1].add(i)

        g[x].add(y)
        g[y].add(x)

        arr = [0]*n
        v = set()

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a == b or (a, b) in v:
                    continue

                v.add((b, a))
                arr[bfs(a, b) - 1] += 2

        return arr
