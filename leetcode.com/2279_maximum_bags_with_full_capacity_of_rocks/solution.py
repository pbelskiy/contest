class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        total = 0
        diff = sorted(a - b for a, b in zip(capacity, rocks))

        for d in diff:
            if d == 0:
                total += 1
            elif additionalRocks >= d:
                additionalRocks -= d
                total += 1
            else:
                break

        return total
