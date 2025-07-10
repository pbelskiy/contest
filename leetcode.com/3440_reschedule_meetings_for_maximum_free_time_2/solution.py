class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        events = list(zip(startTime, endTime))

        # collect gaps
        gaps = []

        gaps.append((events[0][0], 0, events[0][0], (0,)))

        for i in range(len(events) - 1):
            gaps.append((events[i + 1][0] - events[i][1],
                         events[i][1],
                         events[i + 1][0],
                         (i, i + 1)))

        gaps.append((
            eventTime - events[-1][1],
            events[-1][1],
            eventTime,
            (len(events) - 1,)
        ))

        gaps.sort()

        # print(gaps)
        m = gaps[-1][0]

        for i in range(len(events)):
            # left
            if i == 0:
                left = events[i][0]
            else:
                left = events[i][0] - events[i - 1][1]

            # right
            if i == len(events) - 1:
                right = eventTime - events[i][1]
            else:
                right = events[i + 1][0] - events[i][1]

            w = events[i][1] - events[i][0]
            # print(f'{i=} {w=} {left=} {right=}')

            m = max(m, left + right)

            j = bisect.bisect_left(gaps, w,  key=lambda t: t[0])
            while j < len(gaps):
                # print('\tinsert into?', j, gaps[j])
                if i not in gaps[j][-1]:
                    # print('\tOK')
                    m = max(m, left + w + right)
                    break
                j += 1

        return m

