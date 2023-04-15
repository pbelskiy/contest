class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        s, m, a = 0, 0, []

        for n in nums:
            m = max(m, n)
            s += n + m
            a.append(s)

        return a
