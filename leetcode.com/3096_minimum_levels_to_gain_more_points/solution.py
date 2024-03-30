class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        best = float('inf')

        p1, p2 = 0, 0

        for i in range(len(possible)):
            if possible[i] == 0:
                p2 -= 1
            else:
                p2 += 1

        for i in range(len(possible) - 1):
            if possible[i] == 0:
                p1 -= 1
                p2 += 1
            else:
                p1 += 1
                p2 -= 1

            if p1 > p2:
                best = min(best, i + 1)

        if best == float('inf'):
            return -1

        return best
