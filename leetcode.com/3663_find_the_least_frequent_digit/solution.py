class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        return int(sorted([(v, k) for k, v in Counter(str(n)).items()])[0][1])

