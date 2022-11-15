class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = set()

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    arr.add(words[i])

        return arr
