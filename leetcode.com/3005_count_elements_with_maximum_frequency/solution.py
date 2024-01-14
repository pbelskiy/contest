class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)

        m = count.most_common(1)[0][1]
        return sum(v for k, v in count.items() if v == m)
