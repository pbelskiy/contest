class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = {}

        for i, ch in enumerate(s):
            if ch in d:
                d[ch] -= i - 1
            else:
                d[ch] = i

        for k, v in d.items():
            if distance[ord(k) - ord('a')] != abs(v):
                return False

        return True
