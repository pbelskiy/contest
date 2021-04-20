class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0, 1, 1]

        for i in range(3, n + 1):
            seq.append(sum(seq[i-3:i]))

        return seq[n]
