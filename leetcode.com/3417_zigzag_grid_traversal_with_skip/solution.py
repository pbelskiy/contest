class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        arr = []
        i = 0

        for y in range(len(grid)):
            if y % 2 == 1:
                grid[y] = grid[y][::-1]

            for v in grid[y]:
                if i % 2 == 0:
                    arr.append(v)
                i += 1

        return arr
