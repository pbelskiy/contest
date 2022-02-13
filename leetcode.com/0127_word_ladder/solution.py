class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        q = collections.deque([(beginWord, 1)])
        visited = set()

        while q:
            w, d = q.popleft()

            if w == endWord:
                return d

            for i in range(len(w)):
                for ch in string.ascii_lowercase:
                    nw = w[:i] + ch + w[i+1:]
                    if nw in visited:
                        continue
                    if nw in wordList:
                        q.append((nw, d + 1))
                        visited.add(nw)

        return 0
