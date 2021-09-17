class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = collections.Counter(words[0])

        for word in words:
            res &= collections.Counter(word)

        return res.elements()
