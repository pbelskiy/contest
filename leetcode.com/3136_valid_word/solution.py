class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()

        if {'@', '#', '$'} & set(word):
            return False

        if len(word) < 3:
            return False

        vowels = {'a', 'e', 'i', 'o', 'u'}
        consonant = set(string.ascii_lowercase) - vowels

        if not (vowels & set(word)):
            return False

        if not (consonant & set(word)):
            return False

        return True
