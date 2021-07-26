class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        for _s, _e in self.intervals:

            if _s <= start < _e or _s < end <= _e:
                return False

            if start <= _s < end or start < _e <= end:
                return False

        self.intervals.append((start, end))
        # self.sort.intervals()
        return True
