"""
Calculate possible valid indexes of primes and not primes.
Then multiply factorial of it.

Example:
    Array = [1,2,3,4,5] (n = 5)

    Valid indexes of primes:
        [X,2,3,X,5] => 3 positions
    Valid indexes of not primes:
        [1,X,X,4,X] => 2 positions

TC: O(N)
SC: O(1)
"""
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = set([
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
        ])

        a, b = 0, 0

        for i in range(1, n + 1):
            if i in primes:
                a += 1
            else:
                b += 1

        return (factorial(a) * factorial(b)) % (10**9 + 7)
