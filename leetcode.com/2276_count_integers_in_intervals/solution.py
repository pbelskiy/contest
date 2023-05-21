class CountIntervals:

    def __init__(self):
        self.intervals = []  # SortedList()
        self.total = 0

    def add(self, left: int, right: int) -> None:
        # insert
        index = bisect.bisect(self.intervals, [left, right])
        self.intervals.insert(index, [left, right])
        self.total += right - left + 1

        # merge
        i, j = max(0, index - 1), len(self.intervals) - 1
        while i < j:
            if self.intervals[i][1] + 1 < self.intervals[i+1][0]:
                i += 1
                continue

            # calculate difference
            a = self.intervals[i+0][1] - self.intervals[i+0][0] + 1
            b = self.intervals[i+1][1] - self.intervals[i+1][0] + 1
            c = a + b

            self.intervals[i][1] = max(self.intervals[i][1], self.intervals[i+1][1])
            self.total -= c - (self.intervals[i][1] - self.intervals[i][0] + 1)

            # remove next
            self.intervals.pop(i + 1)
            j -= 1

    def count(self) -> int:
        return self.total
