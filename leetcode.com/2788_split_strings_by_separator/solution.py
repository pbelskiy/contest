class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return filter(lambda s: len(s) > 0, separator.join(words).split(separator))
