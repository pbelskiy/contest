class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(i, s, v):
            if s >= target:
                if s == target:
                    combinations.append(v)
                return

            dfs(i, s + candidates[i], v[:] + [candidates[i]])

            if i + 1 < len(candidates):
                dfs(i + 1, s, v[:])

        candidates.sort()
        combinations = []
        dfs(0, 0, [])
        return combinations

