class Solution:
    def scoreBalance(self, s: str) -> bool:
        
        def get_score(ss):
            t = 0
            for ch in ss:
                t += ord(ch) - ord('a') + 1

            return t

        for i in range(1, len(s)):
            if get_score(s[:i]) == get_score(s[i:]):
                return True

        return False

