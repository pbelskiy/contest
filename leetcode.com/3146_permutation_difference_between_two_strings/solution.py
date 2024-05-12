class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(s.index(s[i]) - t.index(s[i])) for i in range(len(s)))
