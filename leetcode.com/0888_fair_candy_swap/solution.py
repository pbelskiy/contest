class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()

        a = sum(aliceSizes)
        b = sum(bobSizes)
        t = (a + b) // 2

        for i in range(len(aliceSizes)):
            need = t - aliceSizes[i]
            j = bisect.bisect(bobSizes, need)

            if a - aliceSizes[i] + bobSizes[j] == b - bobSizes[j] + aliceSizes[i]:
                return [aliceSizes[i], bobSizes[j]]
