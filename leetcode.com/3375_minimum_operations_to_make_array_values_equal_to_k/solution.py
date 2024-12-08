class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0

        while True:
            if set(nums) == {k}:
                return ops

            ops += 1

            result = None
            for h in range(k, max(nums)):
                s = set([n for n in nums if n > h])
                if len(s) == 1:
                    result = h
                    break

            if result is None:
                return -1

            for i in range(len(nums)):
                if nums[i] > result:
                    nums[i] = result

        return -1
