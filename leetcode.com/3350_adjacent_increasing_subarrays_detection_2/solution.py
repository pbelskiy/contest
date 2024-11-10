"""
Greedy, store size of all increasing subarrays, then check
for their adjacent.

TC: O(N)
SC: O(N)
"""
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        a = []
        j = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                a.append(i - j)
                j = i

        a.append(len(nums) - j)

        m = 0
        for i in range(len(a)):
            m = max(m, a[i] // 2)

            if i + 1 < len(a):
                m = max(m, min(a[i], a[i+1]))

        return m
