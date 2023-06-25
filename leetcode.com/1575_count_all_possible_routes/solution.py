class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @cache
        def dp(i, f):
            r = int(i == finish)

            for j in range(len(locations)):
                if j != i and abs(locations[i] - locations[j]) <= f:
                    r += dp(j, f - abs(locations[i] - locations[j]))

            return r % (10**9 + 7)

        return dp(start, fuel) % (10**9 + 7)
