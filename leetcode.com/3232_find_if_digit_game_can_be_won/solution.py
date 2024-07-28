class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1 = s2 = 0

        for n in nums:
            if n < 10:
                s1 += n
            else:
                s2 += n

        return s1 != s2
