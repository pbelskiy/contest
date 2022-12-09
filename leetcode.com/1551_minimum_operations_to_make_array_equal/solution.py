class Solution:
    def minOperations(self, n: int) -> int:
        arr = [0]*n

        for i in range(n):
            arr[i] = (2*i) + 1

        total = 0
        left, right = 0, len(arr) - 1

        while left < right:
            total += (arr[right] - arr[left]) // 2
            left += 1
            right -= 1

        return total
