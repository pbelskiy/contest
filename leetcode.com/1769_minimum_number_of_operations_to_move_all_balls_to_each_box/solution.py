class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ops = [0] * n

        for i in range(n):

            for j in range(0, i):
                ops[i] += abs(i - j) if boxes[j] == '1' else 0

            for j in range(i + 1, n):
                ops[i] += abs(i - j) if boxes[j] == '1' else 0

        return ops
