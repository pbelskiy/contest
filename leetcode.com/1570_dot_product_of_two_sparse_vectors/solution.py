class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def dotProduct(self, vec: 'SparseVector') -> int:
        p = 0

        for a, b in zip(self.nums, vec.nums):
            p += a*b

        return p
