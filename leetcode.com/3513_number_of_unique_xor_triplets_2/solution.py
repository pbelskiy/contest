class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums = set(nums)

        s1 = set()
        for a in nums:
            for b in nums:
                s1.add(a ^ b)

        result = set()
        for x in s1:
            for c in nums:
                result.add(x ^ c)

        return len(result)

