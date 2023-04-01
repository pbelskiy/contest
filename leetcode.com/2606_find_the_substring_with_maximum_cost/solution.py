class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # convert string to array [1, -1000, 1, 1]
        cost = {c: v for c, v in zip(chars, vals)}
        arr = [cost.get(c, ord(c) - ord('a') + 1) for c in s]

        # linear search of largest value (DP)
        dp = [0]*len(arr)
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            dp[i] = max(0, arr[i], dp[i - 1] + arr[i])

        return max(0, max(dp))
