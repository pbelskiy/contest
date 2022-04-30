class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        total = m*n - len(guards) - len(walls)

        grid = [[0]*n for _ in range(m)]

        for y, x in walls:
            grid[y][x] = 1

        for y, x in guards:
            grid[y][x] = 2

        markers = (1, 2)

        for y, x in guards:
            # left
            cx = x - 1
            while cx >= 0:
                if grid[y][cx] in markers:
                    break
                if grid[y][cx] == 0:  # unguarded
                    total -= 1
                    grid[y][cx] = 3   # visited
                cx -= 1

            # right
            cx = x + 1
            while cx < n:
                if grid[y][cx] in markers:
                    break
                if grid[y][cx] == 0:  # unguarded
                    total -= 1
                    grid[y][cx] = 3   # visited
                cx += 1

            # up
            cy = y - 1
            while cy >= 0:
                if grid[cy][x] in markers:
                    break
                if grid[cy][x] == 0:  # unguarded
                    total -= 1
                    grid[cy][x] = 3   # visited
                cy -= 1

            # down
            cy = y + 1
            while cy < m:
                if grid[cy][x] in markers:
                    break
                if grid[cy][x] == 0:  # unguarded
                    total -= 1
                    grid[cy][x] = 3   # visited
                cy += 1

        return total
