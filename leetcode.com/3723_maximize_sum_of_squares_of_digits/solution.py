class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        s = ''

        while num > 0:
            for x in range(9, -1, -1):
                if sum - x >= 0:
                    s += str(x)
                    sum -= x
                    break
            else:
                break

            num -= 1

        if num == 0 and sum == 0:
            return s

        return ''

