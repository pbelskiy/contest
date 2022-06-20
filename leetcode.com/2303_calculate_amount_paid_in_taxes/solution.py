class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        rest = income
        taxes = 0
        prev = 0

        for upper, percent in brackets:
            earn = upper - prev

            if earn > rest:
                earn = income - prev

            taxes += earn*percent/100

            prev = upper
            rest -= earn

            if rest <= 0:
                break

        return taxes
