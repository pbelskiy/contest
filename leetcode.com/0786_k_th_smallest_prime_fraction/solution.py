class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                heappush(h, (arr[i] / arr[j], arr[i], arr[j]))

        while k > 0:
            _, a, b = heappop(h)
            k -= 1

        return [a, b]
