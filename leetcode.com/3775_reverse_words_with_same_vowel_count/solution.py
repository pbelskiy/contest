class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        words = s.split()
        target = sum([int(ch in vowels) for ch in words[0]])

        res = [words[0]]
        for word in words[1:]:
            curr = sum([int(ch in vowels) for ch in word])
            if curr == target:
                res.append(word[::-1])
            else:
                res.append(word)

        return ' '.join(res)

