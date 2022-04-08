class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            a, b = stones.pop(), stones.pop()
            stones.append(abs(a - b))

        return stones[0]
