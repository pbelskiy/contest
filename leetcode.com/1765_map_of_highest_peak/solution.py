"""
Just grow up islands starting from water step by step.

TC: O(NM)
SC: O(NM)
"""
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        h, w = len(isWater), len(isWater[0])

        height = [[-1]*w for _ in range(h)]

        # collect all water cells
        q = deque()
        for y in range(h):
            for x in range(w):
                if isWater[y][x] == 1:
                    q.append((y, x, 0))
                    height[y][x] = 0

        # grow up islands starting from water
        while q:
            y, x, v = q.popleft()

            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if height[dy][dx] == -1:
                    q.append((dy, dx, v + 1))
                    height[dy][dx] = v + 1

        return height
