class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return [k for k, v in Counter([s[i:i+10] for i in range(len(s) - 9)]).items() if v > 1]
