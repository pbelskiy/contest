class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        s = 0

        for i in range(n):
            if grumpy[i] == 0:
                s += customers[i]

        left = 0
        for right in range(minutes):
            if grumpy[right] == 1:
                s += customers[right]

        m = s
        while right < n - 1:
            if grumpy[left]:
                s -= customers[left]
            left += 1

            if grumpy[right + 1]:
                s += customers[right + 1]
            right += 1

            m = max(m, s)

        return m
