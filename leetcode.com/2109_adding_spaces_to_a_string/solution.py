class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        a = []
        i = 0

        for j in spaces:
            a.append(s[i:j])
            i = j

        a.append(s[j:])
        return ' '.join(a)
