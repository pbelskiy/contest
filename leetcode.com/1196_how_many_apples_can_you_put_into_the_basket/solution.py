class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()

        t = 0
        s = 0

        for w in weight:
            if s + w > 5000:
                break
            s += w
            t += 1

        return t
