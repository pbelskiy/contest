class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)

        lonely = []

        for n in nums:
            if count[n] == 1 and count[n - 1] == 0 and count[n + 1] == 0:
                lonely.append(n)

        return lonely
