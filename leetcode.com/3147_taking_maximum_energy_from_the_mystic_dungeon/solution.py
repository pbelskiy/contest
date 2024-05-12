class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        @cache
        def dfs(i):
            return 0 if i >= len(energy) else dfs(i + k) + energy[i]

        return max(dfs(i) for i in range(len(energy)))
