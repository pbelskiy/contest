class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        a, i = set(), 0

        while len(a) != n:
            i += 1
            if k - i in a:
                continue
            a.add(i)

        return sum(a)
