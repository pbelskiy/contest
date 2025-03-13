class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        t = 0

        for f in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= f:
                    baskets[i] = 0
                    break
            else:
                t += 1

        return t

