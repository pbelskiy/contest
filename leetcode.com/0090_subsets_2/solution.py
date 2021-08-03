class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = []
        nums.sort()

        for r in range(len(nums) + 1):
            l.extend(itertools.combinations(nums, r))
        return set(s)
