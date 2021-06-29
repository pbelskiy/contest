class RangeModule:

    def __init__(self):
        self.intervals = []

    def _maintain(self):
        if len(self.intervals) <= 1:
            return

        self.intervals.sort()
        new_intervals = [self.intervals[0]]

        for interval in self.intervals[1:]:
            left, right = interval

            if new_intervals[-1][1] + 1 >= left:
                new_intervals[-1] = (new_intervals[-1][0], max(new_intervals[-1][1], right))
                continue

            new_intervals.append(interval)

        self.intervals = new_intervals

    def addRange(self, left: int, right: int) -> None:
        right -= 1
        self.intervals.append((left, right))
        self._maintain()

    def removeRange(self, left: int, right: int) -> None:
        right -= 1

        new_intervals = []

        for interval in self.intervals:
            _l, _r = interval

            # no overlap
            if min(right, _r) - max(left, _l) < 0:
                new_intervals.append(interval)
                continue

            # full overlap
            if left <= _l and _r <= right:
                continue

            # right overlap
            if _l <= left - 1:
                new_intervals.append((_l, left - 1))

            # left overlap
            if _r >= right + 1:
                new_intervals.append((right + 1, _r))

        self.intervals = new_intervals
        self._maintain()

    def queryRange(self, left: int, right: int) -> bool:
        right -= 1

        for i, interval in enumerate(self.intervals):
            _l, _r = interval
            if _l <= left <= _r and _l <= right <= _r:
                return True

        return False
