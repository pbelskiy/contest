class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()

        total = 0
        ready = []

        _min = min(e[0] for e in events)
        _max = max(e[1] for e in events)

        i = 0

        for day in range(_min, _max + 1):
            if i == len(events) and not ready:
                break

            # collect ready events till current day
            while i < len(events) and events[i][0] <= day <= events[i][1]:
                begin, end = events[i]
                heappush(ready, (end, begin))
                i += 1

            # consume the earliest event which could be finished
            while ready:
                end, begin = heappop(ready)
                if begin <= day <= end:
                    total += 1
                    break

        return total

