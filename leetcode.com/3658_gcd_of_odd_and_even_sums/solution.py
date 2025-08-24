class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = 0
        sum_even = 0

        for i in range(1, n*2 + 1):
            if i % 2 == 0:
                sum_even += i
            else:
                sum_odd += i

        return math.gcd(sum_odd, sum_even)

