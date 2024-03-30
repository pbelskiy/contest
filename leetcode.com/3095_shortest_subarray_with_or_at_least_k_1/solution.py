class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        m = float('inf')

        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s |= nums[j]
                if s >= k:
                    m = min(m, j - i + 1)

        if m == float('inf'):
            return -1

        return m
