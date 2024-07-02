class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def get_power(x):
            s = 0

            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                s += 1

            return s

        a = []
        for x in range(lo, hi + 1):
            a.append((get_power(x), x))

        return sorted(a)[k - 1][1]
