"""
Use monotonic stack here, save in stack value and
count of stock which is lower that current price.

TC: O(1)
SC: O(N)
"""
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        total = 1

        while self.stack and self.stack[-1][-1] <= price:
            t, v = self.stack.pop()
            total += t

        self.stack.append((total, price))
        return total
