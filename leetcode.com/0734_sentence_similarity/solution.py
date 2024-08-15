class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        d = defaultdict(set)
        for a, b in similarPairs:
            d[a].add(b)
            d[b].add(a)

        for a, b in zip(sentence1, sentence2):
            if a == b:
                continue

            if b in d[a] or a in d[b]:
                continue

            return False

        return True
