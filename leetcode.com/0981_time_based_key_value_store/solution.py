class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ''

        bucket = self.d[key]
        left, right = 0, len(bucket)

        while left < right:
            mid = (left + right) // 2
            if timestamp < bucket[mid][0]:
                right = mid
            else:
                left = mid + 1

        if bucket[left - 1][0] > timestamp:
            return ''

        return bucket[left - 1][1]
