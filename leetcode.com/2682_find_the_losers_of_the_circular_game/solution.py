class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        p, i, j = set(), 1, 1

        while j not in p:
            p.add(j)

            j = ((j + (i*k) - 1) % n) + 1

            i += 1

        return sorted(set(range(1, n + 1)) - p)
