"""
Sort, and greedy calculate operations needed.

If median index != k, then go to left or right and
calcualte difference sum.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        n = len(a)

        # get middle index
        i = n // 2
        t = 0
        m = float('inf')

        # reduce values on the left
        if a[i] > k:
            t = 0
            while i >= 0 and a[i] > k:
                t += a[i] - k
                i -= 1

        # increase values on the right
        elif a[i] < k:
            while i < len(a) and a[i] < k:
                t += k - a[i]
                i += 1

        return t
