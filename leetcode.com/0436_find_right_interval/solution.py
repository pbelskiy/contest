class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        s, r = sorted([(*intervals[i], i) for i in range(len(intervals))]), []

        for start, end in intervals:
            lo, hi = 0, len(s) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if s[mid][0] < end:
                    lo = mid + 1
                else:
                    hi = mid - 1

            if lo == len(s):
                r.append(-1)
            else:
                r.append(s[lo][2])

        return r
