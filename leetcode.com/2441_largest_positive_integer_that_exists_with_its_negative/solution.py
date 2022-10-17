class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        m = float('-inf')

        for n in s:
            if -n in s:
                m = max(m, abs(n))

        return m if m != float('-inf') else -1
