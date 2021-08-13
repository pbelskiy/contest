class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0

        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1

        return count
