class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @functools.cache
        def go(s_idx, t_idx):
            # end of t string, so new 1 match found
            if t_idx > t_len:
                return 1

            # end of s string, so it`s still no matches
            if s_idx > s_len:
                return 0

            count = go(s_idx + 1, t_idx + 0)

            if s[s_idx] == t[t_idx]:
                count += go(s_idx + 1, t_idx + 1)

            return count

        s_len, t_len = len(s) - 1, len(t) - 1
        return go(0, 0)
