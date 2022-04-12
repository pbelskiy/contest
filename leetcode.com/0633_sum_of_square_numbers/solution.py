class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            val = left**2 + right**2

            if val == c:
                return True

            if val < c:
                left += 1
            else:
                right -= 1

        return False
