class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        cnt = collections.Counter()

        for a, b in logs:
            for year in range(a, b):
                cnt[year] += 1

        res = float('inf')
        last_count = None

        for year, count in cnt.most_common():
            if last_count and count < last_count:
                break

            res = min(res, year)
            last_count = count

        return res
