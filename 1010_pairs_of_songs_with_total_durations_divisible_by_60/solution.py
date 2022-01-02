class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        total, p = 0, [0] * 60

        for t in time:
            i = -t % 60
            total += p[(60 - i) % 60]
            p[i] += 1

        return total
