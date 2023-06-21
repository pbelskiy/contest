"""
Seems it's esier to choce some existed num from array,
getting total cost by sorted array gives us also sorted
total cost, so we just find optimal result going from mid.

TC: O(NlogN)
SC: O(logN)
"""

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        def get(n):
            t = 0
            for i in range(len(nums)):
                if nums[i] != n:
                    t += abs(nums[i] - n)*cost[i]
            return t

        sn = sorted(nums)
        r = float('inf')

        # from mid to left
        i = len(sn) // 2
        while i >= 0:
            v = get(sn[i])
            if v > r:
                break
            r = v
            i -= 1

        # from mid to right
        i = len(sn) // 2
        while i < len(sn):
            v = get(sn[i])
            if v > r:
                break
            r = v
            i += 1

        return r
