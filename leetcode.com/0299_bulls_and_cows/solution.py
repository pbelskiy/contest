class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = Counter(guess)
        a, b = 0, 0

        for ch1, ch2 in zip(secret, guess):
            if ch1 != ch2:
                continue

            count[ch1] -= 1
            a += 1

        for ch1, ch2 in zip(secret, guess):
            if ch1 == ch2:
                continue

            if count[ch1] > 0:
                count[ch1] -= 1
                b += 1

        return f'{a}A{b}B'
