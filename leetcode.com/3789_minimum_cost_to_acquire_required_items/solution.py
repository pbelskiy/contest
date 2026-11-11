class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 > need2:
            m = (need1 - need2)*cost1 + need2*costBoth
        else:
            m = (need2 - need1)*cost2 + need1*costBoth

        return min(
            m,
            costBoth * max(need1, need2),
            cost1*need1 + cost2*need2,
        )

