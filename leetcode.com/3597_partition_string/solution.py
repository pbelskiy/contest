"""
Linear solution with hashmap.

TC: O(N)
SC: O(N)
"""
class Solution:
    def partitionString(self, s: str) -> List[str]:
        d = {}
        p = ''

        for i in range(len(s)):
            p += s[i]

            if p not in d:
                d[p] = True
                p = ''

        return list(d)

