class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        drunk = numBottles

        while empty >= numExchange:
            drunk += empty // numExchange
            empty = (empty // numExchange) + (empty % numExchange)

        return drunk
