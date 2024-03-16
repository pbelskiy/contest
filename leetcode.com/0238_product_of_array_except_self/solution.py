class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        p = 1
        for n in nums:
            p *= n
            prefix.append(p)

        suffix = []
        p = 1
        for n in reversed(nums):
            p *= n
            suffix.append(p)

        suffix = suffix[::-1]

        answer = []
        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 1
            right = suffix[i + 1] if i + 1 < len(nums) else 1
            answer.append(left * right)

        return answer
