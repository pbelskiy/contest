"""
Use bisect over BFS. 

We even don't need bisect here due to low constrainst.

TC: O(N^2*lgN)
SC: O(N^2)
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        def is_possible(t):
            if grid[0][0] > t:
                return False

            q = deque([(0, 0)])
            v = set(q)
            while q:
                y, x = q.popleft()

                if y == len(grid) - 1 and x == len(grid[0]) - 1:
                    return True

                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if not (0 <= dy < len(grid) and 0 <= dx < len(grid[0])):
                        continue
                    if (dy, dx) in v:
                        continue

                    if grid[dy][dx] > t:
                        continue

                    v.add((dy, dx))
                    q.append((dy, dx))

            return False

        lo = min(min(row) for row in grid)
        hi = max(max(row) for row in grid)
        
        while lo <= hi:
            t = (lo + hi) // 2
            if is_possible(t):
                hi = t - 1
            else:
                lo = t + 1

        return lo

