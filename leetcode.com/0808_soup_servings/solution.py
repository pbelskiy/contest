class Solution:
    def soupServings(self, n: int) -> float:

        @cache
        def dfs(a, b):
            if a == 0 and b == 0:
                return 0.5

            if a == 0:
                return 1.0

            if b == 0:
                return 0.0

            # print(a, b)

            # pour 100 mL from type A and 0 mL from type B
            p1 = dfs(max(0, a - 4), b)

            # pour 75 mL from type A and 25 mL from type B
            p2 = dfs(max(0, a - 3), max(0, b - 1))

            # pour 50 mL from type A and 50 mL from type B
            p3 = dfs(max(0, a - 2), max(0, b - 2))

            # pour 25 mL from type A and 75 mL from type B
            p4 = dfs(max(0, a - 1), max(0, b - 3))

            # print(p1, p2, p3, p4)
            return 0.25 * (p1 + p2 + p3 + p4)

        if n >= 15751:
            return 1.0

        return dfs(n / 25, n / 25)

