"""
Count frequncy and use simple logic for calculation.

TC: O(N)
SC: O(N)
"""
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        f = Counter(answers)
        t = 0

        for k, v in f.items():
            if k == 0:
                t += v
                continue

            if k >= v:
                t += k + 1
                continue

            g = math.ceil(v / (k + 1))
            t += g*(k+1)

        return t

