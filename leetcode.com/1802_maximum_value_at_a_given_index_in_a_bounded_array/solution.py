class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = index, index

        value = 1
        total = n

        if n < maxSum:
            value += 1
            total += 1

        while True:
            left = max(0, left - 1)
            right = min(n - 1, right + 1)

            width = right - left + 1
            total += width

            if total > maxSum:
                break

            value += 1

            # bounds limit
            if left == 0 and right == n - 1:
                value += ((maxSum - total) // n)
                break

        return value
