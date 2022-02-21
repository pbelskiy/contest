class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = len(nums) // 3
        r = []

        for k, v in collections.Counter(nums).most_common():
            if v > m:
                r.append(k)

        return r
