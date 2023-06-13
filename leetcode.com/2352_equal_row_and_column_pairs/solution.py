class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = Counter(), Counter()

        for row in grid:
            rows[tuple(row)] += 1

        for col in list(zip(*grid)):
            cols[tuple(col)] += 1

        total = 0
        for row, num in rows.items():
            total += num*cols[row]

        return total
