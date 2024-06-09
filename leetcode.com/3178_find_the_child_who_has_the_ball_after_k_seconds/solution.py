class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        a = list(range(n))

        while len(a) < k*2:
            a.extend(list(range(n - 2, -1, -1)))
            a.extend(list(range(1, n)))

        return a[k]
