"""
Collect bits position

TC: O(N)
SC: O(N)
"""
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        dist = defaultdict(deque)
        bits = math.floor(math.log2(max(nums) + 1)) + 1

        # collect bits positions
        for i in range(len(nums)):
            for x in range(bits):
                if (1 << x) & nums[i]:
                    dist[x].append(i)

        # calc
        answer = []

        for i in range(len(nums)):
            m = 0

            # find needed bits
            for x in range(bits):
                if dist[x] and not ((1 << x) & nums[i]):
                    m = max(m, dist[x][0])

            # no bits needed, we are already num at current position
            if m == 0:
                answer.append(1)
            else:
                answer.append(m - i + 1)

            # decrease available bits
            for x in range(bits):
                if (1 << x) & nums[i]:
                    if dist[x] and dist[x][0] >= i:
                        dist[x].popleft()

        return answer

