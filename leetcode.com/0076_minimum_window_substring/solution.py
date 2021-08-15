class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        sd = collections.Counter()
        td = collections.Counter(t)

        left, right = 0, 0
        i, j = 0, 0

        matches = 0

        while left < len(s):
            # increase
            if matches < len(td) and right < len(s):
                ch = s[right]
                sd[ch] += 1
                if sd[ch] == td[ch]:
                    matches += 1
                right += 1

            # decrease
            else:
                ch = s[left]
                sd[ch] -= 1
                if sd[ch] < td[ch]:
                    matches -= 1
                left += 1

            # update minimal substring
            if matches == len(td):
                if (right - left) < (j - i) or j == 0:
                    i = left
                    j = right

        return s[i:j]
