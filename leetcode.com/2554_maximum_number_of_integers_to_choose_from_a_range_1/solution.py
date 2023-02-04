class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b = set(banned)
        s, t = 0, 0

        for i in range(1, n + 1):
            if i in b:
                continue
            if s + i > maxSum:
                break
            s += i
            t += 1

        return t
