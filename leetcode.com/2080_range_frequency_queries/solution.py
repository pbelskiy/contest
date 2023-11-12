class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        count = defaultdict(int)
        first = {}
        last = {}

        for i in range(len(arr)):
            if count[arr[i]] == 0:
                first[arr[i]] = i
            count[arr[i]] += 1
            last[arr[i]] = (i, count[arr[i]])

        self.first = first
        self.last = last

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.first:
            return 0

        first = self.first[value]
        last, count = self.last[value]

        if right < first:
            return 0
        if right == first:
            return 1
        if left <= first and right >= last:
            return count

        left = max(left, first)
        right = min(last, right)

        return self.arr[left:right+1].count(value)
