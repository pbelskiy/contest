class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = 0

        for n in nums:
            if n % 2 == 0:
                s += n

        r = []
        for n, i in queries:
            if nums[i] % 2 == 0:
                s -= nums[i]

            nums[i] += n

            if nums[i] % 2 == 0:
                s += nums[i]

            r.append(s)

        return r
