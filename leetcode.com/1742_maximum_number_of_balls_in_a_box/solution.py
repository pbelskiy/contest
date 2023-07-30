class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = Counter()

        for n in range(lowLimit, highLimit + 1):
            value = sum(map(int, list(str(n))))
            boxes[value] += 1

        return boxes.most_common(1)[0][1]
