class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for w in words:
            j = s.find(w)
            if s == '' or j != 0:
                break

            s = s[j+len(w):]

        return s == ''
