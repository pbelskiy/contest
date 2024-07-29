class Solution:
    def numTeams(self, r: List[int]) -> int:

        @cache
        def dp1(i, t):
            if t == 3:
                return 1
            s = 0
            for j in range(i + 1, len(r)):
                if r[j] > r[i]:
                    s += dp1(j, t + 1)
            return s

        @cache
        def dp2(i, t):
            if t == 3:
                return 1
            s = 0
            for j in range(i + 1, len(r)):
                if r[j] < r[i]:
                    s += dp2(j, t + 1)
            return s

        s1 = sum(dp1(i, 1) for i in range(len(r)))
        s2 = sum(dp2(i, 1) for i in range(len(r)))

        return s1 + s2
