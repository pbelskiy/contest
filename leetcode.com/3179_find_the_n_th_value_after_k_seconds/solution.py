class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        a = [1]*n

        for _ in range(k):
            for i in range(1, len(a)):
                a[i] = (a[i] + a[i - 1]) % (10**9 + 7)

        return a[n - 1]
