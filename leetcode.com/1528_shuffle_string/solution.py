class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = [-1] * len(s)

        for i, с in enumerate(s):
            l[indices[i]] = s[i]

        return ''.join(l)

