class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        a = list(map(int, str(n)))
        s = sum(a)

        if s <= target:
            return 0

        d = 1
        t = 0

        while s > target:
            v = 10 - a[len(a) - d]

            s -= a[len(a) - d]
            s += 1

            t += v*(10**(d - 1))

            a[len(a) - (d + 1)] += 1
            d += 1

        return t
