class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')

        for i, word in enumerate(words):
            if word[0].lower() in {'a', 'e', 'i', 'o', 'u'}:
                new_word = word + 'ma'
            else:
                new_word = word[1:] + word[0] + 'ma'

            words[i] = new_word + 'a'*(i + 1)

        return ' '.join(words)
