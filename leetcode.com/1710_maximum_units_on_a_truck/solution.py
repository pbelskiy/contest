class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total = 0

        for (boxes, items) in sorted(boxTypes, key=lambda bt: bt[1], reverse=True):
            total += items * min(boxes, truckSize)
            truckSize -= min(boxes, truckSize)

            if truckSize == 0:
                break

        return total
