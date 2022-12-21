class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = defaultdict(list)

        for s in sorted(dictionary, key=len):
            d[s[0]].append(s)

        words = sentence.split()
        for i in range(len(words)):
            bucket = d[words[i][0]]
            if not bucket:
                continue

            for w in bucket:
                if words[i].startswith(w):
                    words[i] = w
                    break

        return ' '.join(words)
