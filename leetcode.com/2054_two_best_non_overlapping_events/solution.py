class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        # save the highest value to the right
        highest_value = [0]*len(events)
        v = events[-1][2]
        for i in range(len(events) - 1, -1, -1):
            v = max(v, events[i][2])
            highest_value[i] = v

        best = 0
        for i in range(len(events)):
            best = max(best, events[i][2])

            # use bisect to find first valid event after current
            lo, hi = i + 1, len(events) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if events[mid][0] > events[i][1]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            if lo < len(events):
                best = max(best, events[i][2] + highest_value[lo])

        return best
