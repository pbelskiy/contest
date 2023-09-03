class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:

        def get(k, trim):
            h = []

            for i, n in enumerate(nums):
                heappush(h, (int(n[-trim:]), i))

            while k > 0:
                n, i = heappop(h)
                k -= 1

            return i

        answer = []
        for k, trim in queries:
            answer.append(get(k, trim))

        return answer
