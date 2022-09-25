class Solution:
    def countEven(self, num: int) -> int:
        total = 0

        for n in range(1, num + 1):
            if sum(map(int, list(str(n)))) % 2 == 0:
                total += 1

        return total
