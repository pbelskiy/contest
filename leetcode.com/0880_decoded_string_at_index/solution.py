# DRAFT OF CODE

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        d = {}
        # parse
        word = ''
        reset = False

        for ch in s:
            if not ch.isdigit():
                if reset:
                    word = ''
                    reset = False

                word += ch
                continue

            if word in d:
                d[word] *= int(ch)
            else:
                d[word] = int(ch)

            reset = True

        print(d)

        # calculate
        prev_len = 0

        for word, count in d.items():
            length = len(word) * count

            if k > length:
                k %= length
                continue

            return word[k % len(word) - 1]
