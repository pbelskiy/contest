class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        total = 0
        words = sorted([word[::-1] for word in words])


        for i in range(len(words)):
            remove = False

            for j in range(i + 1, len(words)):
                if words[j][0] != words[i][0]:
                    break

                if words[j].startswith(words[i]):
                    remove = True

            if not remove:
                total += len(words[i]) + 1

        return total
