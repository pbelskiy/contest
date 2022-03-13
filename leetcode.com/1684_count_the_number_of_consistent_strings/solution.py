class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return len(list(filter(lambda w: len(set(w) | set(allowed)) == len(allowed), words)))
