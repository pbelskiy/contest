class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        total = [0, 0]

        for v in Counter(nums).values():
            total[0] += v // 2
            total[1] += v % 2

        return total
