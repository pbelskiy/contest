class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = {}

        for n in nums:
            d[n] = int(''.join([str(mapping[int(ch)]) for ch in str(n)]))

        return sorted(nums, key=lambda n: d[n])
