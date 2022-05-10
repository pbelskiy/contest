class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(val, rest, total, comb):
            if total < 0:
                return

            if rest == 0:
                if total == 0:
                    self.combinations.append(comb)
                return

            for next_val in range(val + 1, 10):
                dfs(next_val, rest - 1, total - next_val, comb[:] + [next_val])

        self.combinations = []
        dfs(0, k, n, [])
        return self.combinations
