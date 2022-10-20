class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = []

        for i in range(1, (n // 2) +1):
            a.extend([i, -i])

        if n % 2 == 1:
            a.append(0)

        return a
