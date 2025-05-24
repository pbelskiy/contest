class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:

        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            sqrt_n = int(n ** 0.5) + 1
            for i in range(3, sqrt_n, 2):
                if n % i == 0:
                    return False
            return True

        t = 0
        h = []
        v = set()

        for i in range(len(s)):
            for j in range(i, len(s)):
                n = int(s[i:j+1])
                if is_prime(n) and n not in v:
                    heapq.heappush(h, -n)
                    v.add(n)

        for _ in range(3):
            if h:
                t += heapq.heappop(h)

        return -t
