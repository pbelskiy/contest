class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        vi = 0
        scope = 1

        for i, n in enumerate(self.nums):
            if n != target:
                continue

            # reservoir sampling
            if random.random() < 1 / scope:
                vi = i

            scope += 1

        return vi
