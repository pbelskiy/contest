class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        t = 0

        for i in range(len(nums)):
            f = Counter()
            for j in range(i, len(nums)):
                f[nums[j]] += 1
                if f[target] > (j - i + 1) - f[target]:
                    t += 1

        return t

