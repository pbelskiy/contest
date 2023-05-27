class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        @cache
        def dfs(i, s, v):
            if s == target and v not in combinations:
                combinations.append(v)
                return

            if i >= len(candidates) or s >= target:
                return

            dfs(i + 1, s, v)
            dfs(i + 1, s + candidates[i], v + (candidates[i],))

        candidates.sort()
        combinations = []
        dfs(0, 0, ())
        return combinations
