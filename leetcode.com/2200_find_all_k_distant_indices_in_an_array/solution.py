class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        r = []
        x = [j for j in range(len(nums)) if nums[j] == key]

        for i in range(len(nums)):
            for j in x:
                if abs(i - j) <= k:
                    r.append(i)
                    break

        return r
