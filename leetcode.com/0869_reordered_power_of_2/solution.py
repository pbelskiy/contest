class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = sorted(str(n))

        for i in range(31):  # 10^9
            if sorted(str(2**i)) == target:
                return True

        return False
