class Solution:
    def fillCups(self, amount: List[int]) -> int:
        total = 0

        while sum(amount) > 0:
            amount.sort()
            amount[1] -= 1 if amount[1] > 0 else 0
            amount[2] -= 1 if amount[2] > 0 else 0
            total += 1

        return total
