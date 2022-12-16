class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        def get(i, j):
            left, right = i, j
            count = 0

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    break
                if s[left] != s[i] or s[right] != s[j]:
                    break
                left -= 1
                right += 1
                count += 1

            return count

        total = 0
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                continue
            total += get(i, i + 1)

        return total
