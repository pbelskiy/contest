class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_v = min_i = float('inf')
        max_v = max_i = float('-inf')

        for i, n in enumerate(nums):
            if n < min_v:
                min_v, min_i = n, i
            if n > max_v:
                max_v, max_i = n, i

        a, b = min(min_i, max_i), max(min_i, max_i)
        return min(a + len(nums) - b + 1, len(nums) - a, b + 1)
