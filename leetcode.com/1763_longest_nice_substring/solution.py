class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res = ''

        for i in range(len(s)):
            st = set()
            for j in range(i, len(s)):
                st.add(s[j])

                for ch in st:
                    if ch.islower() and ch.upper() not in st:
                        break
                    if ch.isupper() and ch.lower() not in st:
                        break
                else:
                    if j - i + 1 > len(res):
                        res = s[i:j+1]

        return res
