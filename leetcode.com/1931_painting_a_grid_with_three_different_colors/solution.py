"""
Do simply linear recursion with memoization (DP),
but each posision represents column state using
bitmask:

0 - 00 - White
1 - 01 - Red
2 - 10 - Green
3 - 11 - Blue

So it's enough 2*5 = 10 bit to represent column state.

TC: O(M*N)
SC: O(M*N)
"""
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        def get_color(y, p):
            return (p >> (y*2)) & 0b11

        def set_color(y, p, v):
            return p | (v << (y*2))

        @cache
        def dfs(i, p):
            if i == n:
                return 1

            # generate initial y=0 possible bitmasks
            q = deque()
            for v in (1, 2, 3):
                if get_color(0, p) != v:
                    q.append((set_color(0, 0, v), v, 1))

            # generate all possible column states
            qq = deque()
            while q:
                mask, color, y = q.popleft()
                if y == m:
                    qq.append(mask)
                    continue

                for v in (1, 2, 3):
                    # check left and up
                    if get_color(y, p) == v or v == color:
                        continue

                    q.append((set_color(y, mask, v), v, y + 1))

            # use all generated columns
            t = 0
            while qq:
                t += dfs(i + 1, qq.popleft())

            return t % (10**9 + 7)

        return dfs(0, 0)

