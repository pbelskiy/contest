class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        j = -1

        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                if j == -1:
                    j = i
                elif capacity[i] < capacity[j]:
                    j = i

        return j

