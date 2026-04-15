class Solution:
    def minOperations(self, nums: list[int]) -> int:
                
        def sieve_of_eratosthenes(n):
            primes = [True] * (n + 1)
            primes[0] = primes[1] = False
            
            p = 2
            while p * p <= n:
                if primes[p]:
                    for i in range(p * p, n + 1, p):
                        primes[i] = False
                p += 1

            return set([i for i, is_prime in enumerate(primes) if is_prime])
        
        primes = sieve_of_eratosthenes(max(nums)*2)
        ops = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                while nums[i] not in primes:
                    nums[i] += 1
                    ops += 1
            else:
                while nums[i] in primes:
                    nums[i] += 1
                    ops += 1

        return ops

