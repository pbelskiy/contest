class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set(range(1, (len(grid)**2) + 1))
        h = set()
        for row in grid:
            for n in row:
                if n in h:
                    d = n
                h.add(n)

        return [d, list(s - h)[0]]
