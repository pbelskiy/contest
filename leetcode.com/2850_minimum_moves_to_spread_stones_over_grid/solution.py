memo = {}


def grid_cache(f):
    def wrapper(grid):
        key = tuple([tuple(row) for row in grid])
        if key not in memo:
            memo[key] = f(grid)
        return memo[key]
    return wrapper


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        @grid_cache
        def dfs(grid):
            if all(grid[y][x] for y, x in product(range(3), repeat=2)):
                return 0

            m = float('inf')

            for y, x in product(range(3), repeat=2):
                if grid[y][x] > 0:
                    continue

                for dy, dx in product(range(3), repeat=2):
                    if grid[dy][dx] < 2:
                        continue

                    new_grid = deepcopy(grid)
                    new_grid[y][x] += 1
                    new_grid[dy][dx] -= 1
                    m = min(m, dfs(new_grid) + abs(y - dy) + abs(x - dx))

            return m

        return dfs(grid)
