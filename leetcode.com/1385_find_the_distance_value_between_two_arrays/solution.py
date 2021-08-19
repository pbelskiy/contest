class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for n1 in arr1:
            for n2 in arr2:
                if abs(n1 - n2) <= d:
                    break
            else:
                count += 1

        return count
