class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = collections.Counter()

        for i in range(len(nums) - 1):
            if nums[i] == key:
                cnt[nums[i + 1]] += 1

        return cnt.most_common()[0][0]
