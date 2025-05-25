"""
Use stack

TC: O(N)
SC: O(N)
"""
class Solution:
    def resultingString(self, s: str) -> str:
        q = []

        for ch in s:
            if q and abs(ord(ch) - ord(q[-1])) in (1, 25):
                q.pop()
            else:
                q.append(ch)

        return ''.join(q)

