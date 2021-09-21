class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        t, count = 0, 0

        for n in nums:
            if n != 1:
                count = 0
            else:
                count += 1
            t = max(t, count)

        return t
