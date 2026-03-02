class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # collect suffixes
        suffix = []

        for row in grid:
            t = 0
            for i in range(len(row) - 1, -1, -1):
                if row[i] == 1:
                    break
                t += 1
            suffix.append(t)

        # check possibility
        for i, v in enumerate(sorted(suffix)):
            if not (v >= i):
                return -1

        # swap
        t = 0

        done = False
        while not done:
            done = True
            for i in range(len(suffix) - 1):
                need = n - i - 1
                # current row already sorted
                if suffix[i] >= need:
                    continue

                done = False
                # find nearest needed row
                for j in range(i + 1, len(suffix)):
                    if suffix[j] >= need:
                        t += j - i
                        suffix.insert(i, suffix.pop(j))
                        break

        return t

