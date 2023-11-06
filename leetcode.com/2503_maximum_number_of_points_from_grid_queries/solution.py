"""
The main idea here is to start from smalles query to largest query,
and step by step increase area of BFS coverage, and for optimization
need to use heap to reduce operations.
"""

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        def bfs(t, q, v):
            nv = set()
            while q:
                n, y, x = heappop(q)
                if n >= t:
                    heappush(q, (n, y, x))
                    break
                else:
                    v.add((y, x))

                for y, x in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if not (0 <= y < h and 0 <= x < w):
                        continue

                    if grid[y][x] >= t:
                        if (y, x) not in nv:
                            heappush(q, (grid[y][x], y, x))
                            nv.add((y, x))
                        continue

                    if (y, x) in v:
                        continue

                    heappush(q, (grid[y][x], y, x))
                    v.add((y, x))

            return q, v

        h, w = len(grid), len(grid[0])
        answer = [0]*len(queries)
        q, v = [(grid[0][0], 0, 0)], set()
        for t, i in sorted((t, i) for i, t in enumerate(queries)):
            q, v = bfs(t, q, v)
            answer[i] = len(v)

        return answer
