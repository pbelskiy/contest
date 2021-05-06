class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        total = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

        for i in range(L, R + 1):
            count = 0
            for shift in range(20):
                count += (i >> shift) & 1

            total += int(count in primes)

        return total
