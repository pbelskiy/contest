class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid[0])

        # disassemble
        g = []
        for r in grid:
            g.extend(r)

        # shift
        k %= len(g)
        g = g[-k:] + g[:-k]

        # assemble
        grid = []
        for i in range(0, len(g), n):
            grid.append(g[i:i+n])

        return grid
