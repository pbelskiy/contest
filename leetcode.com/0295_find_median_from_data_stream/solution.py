class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        i = len(self.nums) // 2

        if len(self.nums) % 2 == 1:
            return self.nums[i]

        return (self.nums[i - 1] + self.nums[i]) / 2
