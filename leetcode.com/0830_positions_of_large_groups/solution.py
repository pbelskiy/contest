class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        groups = []

        i = 0

        while i < len(s):
            ch = s[i]

            j = i
            while j < len(s) and s[j] == ch:
                j += 1

            if j - i >= 3:
                groups.append([i, j - 1])

            i = j

        return groups
