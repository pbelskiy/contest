class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        @cache
        def dp(i):
            if i >= len(jobs):
                return 0

            k = bisect.bisect_left(jobs, jobs[i][1], key=lambda t: t[0])
            return max(dp(k) + jobs[i][2], dp(i + 1))

        jobs = sorted(zip(startTime, endTime, profit))
        return dp(0)
