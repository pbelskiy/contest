class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        d = meetings[0][0] - 1  # from first meeting
        right = meetings[0][1]

        for i in range(1, len(meetings)):
            a, b = meetings[i]
            if a > right:
                d += a - right - 1  # gap between meetings

            right = max(right, b)

        d += days - right  # from last meeting
        return d
