class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        total = 0

        for x in range(len(strs[0])):
            col = [strs[y][x] for y in range(len(strs))]
            if col != sorted(col):
                total += 1

        return total
