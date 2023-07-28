class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for t in timePoints:
            h, m = map(int, t.split(':'))
            times.append(h*60+m)
            times.append(h*60+m + 1440)

        times.sort()

        d = [(times[len(times) - 1] - times[0])]
        for i in range(len(times) - 1):
            d.append((times[i + 1] - times[i]))

        return min(d)
