"""
Difference array

TC: O(N)
SC: O(N)
"""
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # update difference array
        d = [0]*(len(nums) + 1)

        for l, r in queries:
            d[l] += 1
            if r + 1< len(d):
                d[r + 1] -= 1

        # construct difference array
        a = []
        v = 0
        for n in islice(d, len(nums)):
            v += n
            a.append(v)

        # check if can be zero
        for i in range(len(nums)):
            if nums[i] > a[i]:
                return False

        return True
