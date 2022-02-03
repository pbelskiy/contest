class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        uniq = set()

        for word in words:
            uniq.add(''.join([m[ord(ch) - ord('a')] for ch in word]))

        return len(uniq)
