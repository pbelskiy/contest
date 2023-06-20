"""
Here we just count of same diff, and then
check if the max difference*26 larger than k.

Because of each new +1 of same diff increases
our move by 26.

TC: O(N)
SC: O(1)
"""
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        count = Counter()
        for a, b in zip(s, t):
            if a != b:
                count[(ord(b) - ord(a)) % 26] += 1

        m = 0
        for d, v in count.items():
            m = max(m, d + (v - 1)*26)
            if m > k:
                return False

        return True
