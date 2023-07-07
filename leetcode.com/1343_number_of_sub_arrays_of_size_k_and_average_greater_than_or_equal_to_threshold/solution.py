class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        total = sum(arr[:k])

        for i in range(k, len(arr)):
            if total // k >= threshold:
                count += 1

            total += arr[i]
            total -= arr[i - k]

        return count + (total // k >= threshold)
