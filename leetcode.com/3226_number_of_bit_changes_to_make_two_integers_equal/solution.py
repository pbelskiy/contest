class Solution:
    def minChanges(self, n: int, k: int) -> int:
        total = 0

        for i in range(max(n, k).bit_length()):
            v = 1 << i

            if not (n & v) and (k & v):
                return -1

            if n & v == k & v:
                continue

            total += 1

        return total
