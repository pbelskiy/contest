class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        total = 0
        g.sort()
        s.sort()

        i = 0
        j = 0

        while i < len(g) and j < len(s):

            while j < len(s) and g[i] > s[j]:
                j += 1

            while i < len(g) and j < len(s) and g[i] <= s[j]:
                i += 1
                j += 1
                total += 1

        return total
