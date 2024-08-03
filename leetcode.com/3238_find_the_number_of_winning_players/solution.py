class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        count = [Counter() for _ in range(n)]

        for x, y in pick:
            count[x][y] += 1

        t = 0

        for i, d in enumerate(count):
            for k, v in d.items():
                if v > i:
                    t += 1
                    break

        return t
