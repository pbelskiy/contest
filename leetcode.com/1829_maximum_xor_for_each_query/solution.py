class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = 2**maximumBit - 1

        answer = []
        prev = 0

        for n in nums:
            curr = n ^ prev
            answer.append(curr ^ mask)
            prev = curr

        return answer[::-1]
