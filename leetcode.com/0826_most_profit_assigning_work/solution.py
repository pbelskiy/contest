class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty, profit = zip(*sorted(zip(difficulty, profit)))

        @functools.cache
        def get(i):
            return max(profit[:i])

        total = 0
        for w in worker:
            i = bisect.bisect(difficulty, w)
            if i > 0:
                total += get(i)

        return total
