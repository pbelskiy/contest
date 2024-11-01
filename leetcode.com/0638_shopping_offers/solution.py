class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        @cache
        def dfs(a):
            if sum(a) == 0:
                return 0

            m = sum(a[i] * price[i] for i in range(len(a)))

            for s in special:
                *d, p = s
                na = [a[i] - d[i] for i in range(len(a))]
                if min(na) >= 0:
                    m = min(m, dfs(tuple(na)) + p)

            return m

        return dfs(tuple(needs))
