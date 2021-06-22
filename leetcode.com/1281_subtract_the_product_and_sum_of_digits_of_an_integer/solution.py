class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = list(map(int, list(str(n))))
        return math.prod(l) - sum(l)