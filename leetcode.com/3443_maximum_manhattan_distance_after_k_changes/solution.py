class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        best = 0

        # try all diagonals
        for t in (('N', 'W'), ('S', 'W'), ('S', 'E'), ('N', 'E')):

            y, x, r = 0, 0, k
            for ch in s:
                if ch not in t and r > 0:
                    r -= 1
                    ch = t[0]

                if ch == 'N': y -= 1
                if ch == 'S': y += 1
                if ch == 'E': x += 1
                if ch == 'W': x -= 1

                best = max(best, abs(x) + abs(y))

        return best
