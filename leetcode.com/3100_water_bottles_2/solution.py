class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty_count, drunk_count = 0, 0

        while True:
            drunk_count += numBottles
            empty_count += numBottles
            numBottles = 0

            if numExchange > empty_count:
                break

            while empty_count >= numExchange:
                empty_count -= numExchange
                numBottles += 1
                numExchange += 1

        return drunk_count
