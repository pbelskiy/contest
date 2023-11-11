class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        a = sorted([n for row in values for n in row])

        t = 0
        for d, v in enumerate(a, start=1):
            t += d*v

        return t
