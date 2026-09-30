class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        ans = []

        while count:
            for n in sorted(count):
                if count[n] > 0:
                    count[n] -= 1
                    ans.append(n)
                else:
                    del count[n]

        return ans

