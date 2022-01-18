class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0

        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 1:
                i += 2
                continue

            if i + 1 < len(flowerbed) and flowerbed[i + 1] == 1:
                i += 1
            else:
                n -= 1
                i += 2

        return n <= 0
