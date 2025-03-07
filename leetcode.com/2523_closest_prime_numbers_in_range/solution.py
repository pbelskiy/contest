class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def get_primes(n):
            sieve = list(range(n + 1))
            sieve[1] = 0

            for i in sieve:
                if i > 1:
                    for j in range(2*i, len(sieve), i):
                        sieve[j] = 0

            return [n for n in sieve if n != 0]

        p = get_primes(right)
        d = float('inf')
        t = [-1, -1]

        for i in range(bisect.bisect_left(p, left), len(p) - 1):
            a, b = p[i], p[i + 1]

            if b - a < d:
                d = b - a
                t = [a, b]

        return t
