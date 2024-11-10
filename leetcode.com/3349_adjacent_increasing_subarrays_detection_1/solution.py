"""
Greedy, store size of all increasing subarrays, then check
for their adjacent.

TC: O(N)
SC: O(N)
"""
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        a = []
        j = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                a.append(i - j)
                j = i

        a.append(len(nums) - j)

        for i in range(len(a)):
            if a[i] >= k*2:
                return True

            if a[i] >= k and i + 1 < len(a) and a[i+1] >= k:
                return True

        return False
