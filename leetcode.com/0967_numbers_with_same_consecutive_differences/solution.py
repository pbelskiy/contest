class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        def dfs(r, v):
            if r == 0:
                values.add(int(''.join(map(str, v))))
                return

            last = v[-1]

            if last - k >= 0:
                dfs(r - 1, v + [last - k])

            if last + k <= 9:
                dfs(r - 1, v + [last + k])

        values = set()

        for i in range(1, 10):
            dfs(n - 1, [i])

        return values
