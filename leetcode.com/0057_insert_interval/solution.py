class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        a, b = newInterval

        # insert end
        if a > intervals[-1][1]:
            return intervals + [newInterval]

        # insert begin
        if b < intervals[0][0]:
            return [newInterval] + intervals

        left = right = max(1, bisect.bisect_right(intervals, newInterval))

        # insert middle
        if a > intervals[left - 1][1] and b < intervals[right][0]:
            return intervals[:left] + [newInterval] + intervals[right:]

        # merge
        while right < len(intervals) and b >= intervals[right][0]:
            right += 1

        while intervals[left - 1][1] < a:
            left += 1

        intervals[left - 1][0] = min(intervals[left - 1][0], a)
        intervals[left - 1][1] = max(intervals[right - 1][1], b)

        return intervals[:left] + intervals[right:]
