"""
Use prefix sum to optimize brute force.

TC: O(h*w)
SC: O(h*w)
"""
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])

        # calculate prefix sum for each column
        prefix_sum = []
        for x in range(w):
            column = []
            count = Counter()
            for y in range(h):
                count[grid[y][x]] += 1
                column.append([count['X'], count['Y']])
            prefix_sum.append(column)

        # brute force
        total = 0

        for y in range(h):
            count = Counter()
            for x in range(w):
                count['X'] += prefix_sum[x][y][0]
                count['Y'] += prefix_sum[x][y][1]

                if count['X'] > 0 and count['X'] == count['Y']:
                    total += 1

        return total
