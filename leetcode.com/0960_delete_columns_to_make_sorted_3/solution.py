"""
LIS, compare current and prev columns.

TC: O(HW)
SC: O(HW)
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        @cache
        def dfs(curr_idx, prev_idx):
            # no more columns
            if curr_idx == w:  
                return 0

            # skip
            skip = dfs(curr_idx + 1, prev_idx)

            # take
            valid = True
            if prev_idx != -1:
                for y in range(h):
                    if strs[y][curr_idx] < strs[y][prev_idx]:
                        valid = False
                        break

            take = 0
            if valid:
                take = dfs(curr_idx + 1, curr_idx) + 1

            return max(skip, take)

        h, w = len(strs), len(strs[0])
        return w - dfs(0, -1)

