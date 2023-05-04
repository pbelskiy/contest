class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]

        while True:
            n = fib[-1] + fib[-2]
            if n > 10**9:
                break
            fib.append(n)

        total = 0
        i = len(fib) - 1

        while k > 0:
            if k < fib[i]:
                i -= 1

            elif k >= fib[i]:
                k -= fib[i]
                total += 1

        return total
