class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        answer = []

        for i in range(len(nums)):
            s = 0
            for j in range(i + 1, len(nums)):
                if nums[i] % 2 != nums[j] % 2:
                    s += 1
            answer.append(s)
        
        return answer

