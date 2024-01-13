class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tc = Counter(t)
        t = 0

        for k, v in Counter(s).items():
            if tc[k] < v:
                t += v - tc[k]

        return t
