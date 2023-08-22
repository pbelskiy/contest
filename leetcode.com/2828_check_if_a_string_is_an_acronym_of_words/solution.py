class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False

        for a, b in zip(words, s):
            if a[0] != b:
                return False

        return True
