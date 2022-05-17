class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len(list(filter(lambda w: w.startswith(pref), words)))
