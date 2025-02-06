class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s).values()
        odd = sorted(v for v in freq if v % 2 == 1)
        even = sorted(v for v in freq if v % 2 == 0)

        return odd[-1] - even[0]
