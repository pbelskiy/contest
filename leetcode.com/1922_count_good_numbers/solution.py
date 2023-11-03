class Solution:
    def countGoodNumbers(self, n: int) -> int:

        @cache
        def get(v, p):
            if p <= 2:
                return v**p

            return get(v, p // 2) * get(v, (p // 2) + (p % 2)) % (10**9 + 7)

        return get(4, n // 2) * get(5, (n // 2) + (n % 2)) % (10**9 + 7)
