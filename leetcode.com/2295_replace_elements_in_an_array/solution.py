class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)

        for a, b in operations:
            for i in d[a]:
                nums[i] = b
            d[b] = d[a]

        return nums
