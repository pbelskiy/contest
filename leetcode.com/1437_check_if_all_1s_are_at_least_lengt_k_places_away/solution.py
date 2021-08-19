class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        d = None

        for i, n in enumerate(nums):
            if n == 0:
                continue

            if d == None:
                d = i
            elif i - d - 1 < k:
                return False

            d = i

        return True
