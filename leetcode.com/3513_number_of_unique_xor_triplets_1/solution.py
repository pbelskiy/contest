class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        a = [0, 1, 2, 4]

        while len(a) <= len(nums):
            m = a[-1]
            for i in range(m):
                a.append(m*2)

        return a[len(nums)]

