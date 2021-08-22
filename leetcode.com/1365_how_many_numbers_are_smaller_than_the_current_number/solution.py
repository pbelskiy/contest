class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] < nums[i]:
                    count += 1

            answer.append(count)

        return answer
