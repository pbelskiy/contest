
class Solution:
    def smallestValue(self, n: int) -> int:

        def get_prime_factors_sum(n):
            s = 0

            while n % 2 == 0:
                s += 2
                n //= 2

            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while (n % i == 0):
                    s += i
                    n //= i

            if n > 2:
                s += n

            return s

        while True:
            s = get_prime_factors_sum(n)
            if s == n:
                break
            n = s

        return n
