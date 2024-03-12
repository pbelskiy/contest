class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        t = sum(apple)

        for i, cap in enumerate(sorted(capacity, reverse=True)):
            t -= cap
            if t <= 0:
                return i + 1
