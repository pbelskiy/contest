"""
As usual write recursion algorithm and add @cache for memoization
of already calculated results. It's easy way for DP understanding.

TC: O(H*W*K)
SC: O(K)
"""
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        @cache
        def solve(y, x, r):
            # last piece, check for apples
            if r == 0:
                for cy in range(y, h):
                    for cx in range(x, w):
                        if pizza[cy][cx] == 'A':
                            return 1
                return 0

            total = 0

            # go down
            apples = 0
            for cy in range(y, h):
                if apples == 0:
                    apples += pizza[cy][x:].count('A')
                if apples > 0:
                    total += solve(cy + 1, x, r - 1)

            # go right
            apples = 0
            for cx in range(x, w):
                if apples == 0:
                    apples += pizza_rotated[cx][:h-y].count('A')
                if apples > 0:
                    total += solve(y, cx + 1, r - 1)

            return total % (10**9 + 7)

        pizza_rotated = list(zip(*pizza[::-1]))
        h, w = len(pizza), len(pizza[0])
        return solve(0, 0, k - 1)
