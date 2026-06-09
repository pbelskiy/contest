class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        # merge intervals
        intervals.sort(key=lambda t: t[0])
        r = [intervals[0]]

        for i in range(1, len(intervals)):
            begin, end = intervals[i]
            if begin <= r[-1][1]:
                # merge
                r[-1][1] = max(r[-1][1], end)
            else:
                r.append(intervals[i])

        # calc bulbs needed
        b = math.ceil(brightness / 3)

        # calc minimum total energy 
        t = 0
        for i in range(len(r)):
            t += b * ((r[i][1] - r[i][0]) + 1)

        return t

