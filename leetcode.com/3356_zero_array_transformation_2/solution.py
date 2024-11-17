"""
Difference array + Binary search.

TC: O(NlgN)
SC: O(N)
"""
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def is_possible(k):
            # make difference array
            d = [0]*(len(nums) + 1)

            # update difference array
            for l, r, v in islice(queries, k):
                d[l] += v
                if r + 1 < len(d):
                    d[r + 1] -= v

            # create final difference array
            a, v = [], 0
            for i in range(len(d) - 1):
                v += d[i]
                a.append(v)

            # check possibility
            for i in range(len(nums)):
                if nums[i] > a[i]:
                    return False

            return True

        # bisect
        lo, hi = 0, len(queries)
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo if lo <= len(queries) else -1
