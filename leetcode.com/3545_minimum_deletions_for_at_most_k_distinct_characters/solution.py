class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        f = Counter(s)
        d = len(f) - k
        if d <= 0:
            return 0

        t = 0
        for v in sorted(f.values())[:d]:
            t += v

        return t

