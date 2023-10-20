class Solution:
    def numSplits(self, s: str) -> int:
        total, left, right = 0, Counter(), Counter(s)

        for i in range(len(s)):
            left[s[i]] += 1
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]

            if len(left) == len(right):
                total += 1

        return total
