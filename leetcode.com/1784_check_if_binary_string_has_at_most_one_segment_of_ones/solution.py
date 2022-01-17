class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len([p for p in s.split('0') if '1' in p]) == 1
