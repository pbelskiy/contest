"""
There are few types of operations possible:
    00 -> 00
    01 -> 11
    10 -> 11
    11 -> 10

1) So to convert 1 to 0 we need to have one more 1
2) To convert 0 to 1 we need total avaialable `1` > 0.

TC: O(N)
SC: O(N)
"""
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        total = Counter(s)
        diff = ''

        for i in range(len(s)):
            if s[i] != target[i]:
                diff += s[i]

        for ch in sorted(diff):
            if ch == '1' and total['1'] > 1:
                total['1'] -= 1
                continue

            if ch == '0' and total['1'] > 0:
                total['1'] += 1
                continue

            return False

        return True
