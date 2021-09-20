class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        numbers = [1] * n
        p = len(numbers) - 1

        while k > 0:
            v = min(numbers[p] + k - 1, 25)
            numbers[p] += v
            k -= v
            p -= 1

        return ''.join([chr(ord('a') + n - 1) for n in numbers])
