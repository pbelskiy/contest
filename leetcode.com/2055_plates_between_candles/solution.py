class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i, v in enumerate(s) if v == '|']

        res = []

        for left, right in queries:
            i = bisect.bisect_left(candles, left)
            j = bisect.bisect_right(candles, right) - 1

            res.append(max(0, candles[j] - candles[i] - (j - i)))

        return res
