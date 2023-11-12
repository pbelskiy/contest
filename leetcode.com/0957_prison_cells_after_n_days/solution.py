"""
If we look on how cells changed, we noticed that pattern repeated every
14 days, so we just need use mod 14 here.
"""
class Solution:
    def prisonAfterNDays(self, a: List[int], n: int) -> List[int]:
        for _ in range(14 + n % 14):
            new = a[:]
            for i in range(1, 7):
                new[i] = int(a[i - 1] == a[i + 1])

            new[0] = new[-1] = 0
            a = new

        return a
