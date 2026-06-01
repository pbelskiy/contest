class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(k)*v for k, v in Counter(str(n)).items())

