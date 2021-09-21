class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        q = collections.deque()
        visited = set()

        s = ''.join(map(str, board[0] + board[1]))
        q.append((s.index('0'), s, 0))
        visited.add(s)

        while q:
            p, s, m = q.popleft()

            if s == '123450':
                return m

            for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                y, x = p // 3, p % 3

                if not (0 <= y + dy <= 1):
                    continue

                if not (0 <= x + dx <= 2):
                    continue

                np = (y + dy)*3 + (x + dx)

                ns = list(s)
                ns[p], ns[np] = ns[np], ns[p]
                ns = ''.join(ns)

                if ns not in visited:
                    visited.add(ns)
                    q.append((np, ns, m + 1))

        return -1
