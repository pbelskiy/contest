class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter()
        first, last = {}, {}

        for i, n in enumerate(nums):
            count[n] += 1
            if n in first:
                last[n] = i
            else:
                last[n] = i
                first[n] = i

        degree = None
        smallest = float('inf')

        for k, v in count.most_common():
            if degree is None:
                degree = v
            elif v != degree:
                break

            smallest = min(smallest, last[k] - first[k] + 1)

        return smallest
