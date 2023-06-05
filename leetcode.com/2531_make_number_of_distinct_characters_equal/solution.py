class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1, count2 = Counter(word1), Counter(word2)

        for ch1, ch2 in product(string.ascii_lowercase, string.ascii_lowercase):

            if ch1 not in count1 or ch2 not in count2:
                continue

            count1[ch1] -= 1
            count1[ch2] += 1
            count2[ch1] += 1
            count2[ch2] -= 1

            count1 |= Counter()
            count2 |= Counter()

            if len(count1) == len(count2):
                return True

            count1[ch1] += 1
            count1[ch2] -= 1
            count2[ch1] -= 1
            count2[ch2] += 1

            count1 |= Counter()
            count2 |= Counter()

        return False
