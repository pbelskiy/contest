class Solution:
    def countMonobit(self, n: int) -> int:
        return sum(len(set(bin(i)[2:])) == 1 for i in range(n + 1))

