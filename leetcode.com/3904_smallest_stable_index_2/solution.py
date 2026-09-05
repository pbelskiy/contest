"""
Pre calculated min and max

TC: O(N)
SC: O(N)
"""
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        _max = []
        m = float('-inf')
        for n in nums:
            m = max(m, n)
            _max.append(m)

        _min = []
        m = float('+inf')
        for n in reversed(nums):
            m = min(m, n)
            _min.append(m)

        for i in range(len(nums)):
            if (_max[i] - _min[len(nums) - i - 1]) <= k:
                return i

        return -1

