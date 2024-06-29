class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = list(range(1, n + 1))
        i = 0

        while len(q) > 1:
            i = (i + k - 1) % len(q)
            q.pop(i)

        return q[0]
