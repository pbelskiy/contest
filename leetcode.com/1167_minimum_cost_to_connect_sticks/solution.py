class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0

        heapq.heapify(sticks)
        while len(sticks) > 1:
            a, b = heapq.heappop(sticks), heapq.heappop(sticks)
            heapq.heappush(sticks, a + b)
            cost += a + b

        return cost
