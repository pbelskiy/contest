class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 == 0:
            return 100 - purchaseAmount

        # roundedAmount is a multiple of 10
        # abs(roundedAmount - purchaseAmount) is minimized.

        roundedAmount = float('inf')
        mini = float('inf')

        for m in range(11):
            ra = m*10

            va = abs(ra - purchaseAmount)

            if va <= mini:
                mini = va
                roundedAmount = ra

        return 100 - roundedAmount
