class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        q = collections.deque()
        candidates = []
        h, w = len(grid), len(grid[0])
        low, high = pricing
        visited = set()

        q.append((1, start[0], start[1]))
        visited.add((start[0], start[1]))

        if low <= grid[start[0]][start[1]] <= high:
            candidates.append((1, start[0], start[1]))

        while q:
            d, y, x = q.popleft()

            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):

                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if (dy, dx) in visited:
                    continue

                if grid[dy][dx] == 0:
                    continue

                if low <= grid[dy][dx] <= high:
                    candidates.append((d + 1, dy, dx))

                visited.add((dy, dx))
                q.append((d + 1, dy, dx))

        candidates.sort(key=lambda k: (k[0], grid[k[1]][k[2]], k[1], k[2]))
        return [[candidates[i][1], candidates[i][2]] for i in range(min(k, len(candidates)))]
