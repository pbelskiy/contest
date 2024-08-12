class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []

        for word in words:
            i = 0
            while True:
                i = text.find(word, i)
                if i == -1:
                    break
                res.append([i, i + len(word) - 1])
                i += 1

        return sorted(res)
