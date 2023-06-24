class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        v = set()

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][::-1] and j not in v:
                    v.add(j)
                    break

        return len(v)
