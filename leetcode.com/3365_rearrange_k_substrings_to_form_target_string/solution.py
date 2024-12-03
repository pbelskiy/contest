"""
Get size of chunk, then compare all change from s to t.

TC: O(N)
SC: O(N)
"""
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(t) // k
        count1 = Counter(s[i:i+n] for i in range(0, len(s), n))
        count2 = Counter(t[i:i+n] for i in range(0, len(t), n))
        return count1 == count2
