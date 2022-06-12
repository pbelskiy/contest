class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        for spell in spells:
            lo, hi = 0, len(potions) - 1

            while lo <= hi:
                mid = (hi + lo) // 2
                val = potions[mid]*spell

                if val < success:
                    lo = mid + 1
                elif val >= success:
                    hi = mid - 1

            # last element
            if mid == len(potions) - 1 and val < success:
                mid += 1

            if mid < len(potions) - 1 and val < success:
                mid += 1

            res.append(len(potions) - mid)

        return res
