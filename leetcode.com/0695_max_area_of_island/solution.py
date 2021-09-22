class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        height, width = len(grid), len(grid[0])


        for y in range(height):
            for x in range(width):

                if grid[y][x] == 0 or (y, x) in visited:
                    continue

                area = 1
                q = collections.deque([(y, x)])
                visited.add((y, x))

                while q:
                    y, x = q.popleft()

                    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        ny, nx = y + dy, x + dx

                        if not (0 <= ny < height and 0 <= nx < width):
                            continue

                        if (ny, nx) in visited:
                            continue

                        visited.add((ny, nx))

                        if grid[ny][nx] == 1:
                            q.append((ny, nx))
                            area += 1

                max_area = max(max_area, area)

        return max_area
