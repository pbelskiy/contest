class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f = lambda s: int(''.join(map(str, [ord(ch) - ord('a') for ch in s])))
        return f(firstWord) + f(secondWord) == f(targetWord)
